import os, time, threading
import hashlib, pefile, array, math
import pickle, joblib

from db import DB





class ScanVirusAI:
	def get_entropy(self, data):
		if len(data) == 0: return 0.0

		occurences = array.array('L', [0] * 256)

		for x in data:
			if isinstance(x, int): occurences[x] += 1
			else: occurences[ord(x)] += 1

		entropy = 0
		for x in occurences:
			if x:
				entropy -= float(x)/len(data) * math.log(p_x, 2)

		return entropy

	def get_resources(self, pe):
		resources = []
		if hasattr(pe, 'DIRECTORY_ENTRY_RESOURCE'):
			try:
				for resource_type in pe.DIRECTORY_ENTRY_RESOURCE.entries:
					if hasattr(resource_type, 'directory'):
						for resource_id in resource_type.directory.entries:
							if hasattr(resource_id, 'directory'):
								for resource_lang in resource_id.directory.entries:
									data = pe.get_data(resource_lang.data.struct.OffsetToData, resource_lang.data.struct.Size)
									size = resource_lang.data.struct.Size
									entropy = self.get_entropy(data)
									resources.append([entropy, size])
			except:
				return resources

		return resources

	def get_version_info(self, pe):
		res = {}

		for fileinfo in pe.FileInfo:

			if fileinfo.Key == 'StringFileInfo':
				for st in fileinfo.StringTable:
					for entry in st.entries.items():
						res[entry[0]] = entry[1]

			if fileinfo.Key == 'VarFileInfo':
				for var in fileinfo.Var:
					res[var.entry.items()[0][0]] = var.entry.items()[0][1]


		if hasattr(pe, 'VS_FIXEDFILEINFO'):
			res['flags'] = pe.VS_FIXEDFILEINFO.FileFlags
			res['os'] = pe.VS_FIXEDFILEINFO.FileOS
			res['type'] = pe.VS_FIXEDFILEINFO.FileType
			res['file_version'] = pe.VS_FIXEDFILEINFO.FileVersionLS
			res['product_version'] = pe.VS_FIXEDFILEINFO.ProductVersionLS
			res['signature'] = pe.VS_FIXEDFILEINFO.Signature
			res['struct_version'] = pe.VS_FIXEDFILEINFO.StrucVersion

		return res

	def extract_infos(self, fpath, clf, features):
		res = {}
		pe = pefile.PE(fpath)
		res['Machine'] = pe.FILE_HEADER.Machine
		res['SizeOfOptionalHeader'] = pe.FILE_HEADER.SizeOfOptionalHeader
		res['Characteristics'] = pe.FILE_HEADER.Characteristics
		res['MajorLinkerVersion'] = pe.OPTIONAL_HEADER.MajorLinkerVersion
		res['MinorLinkerVersion'] = pe.OPTIONAL_HEADER.MinorLinkerVersion
		res['SizeOfCode'] = pe.OPTIONAL_HEADER.SizeOfCode
		res['SizeOfInitializedData'] = pe.OPTIONAL_HEADER.SizeOfInitializedData
		res['SizeOfUninitializedData'] = pe.OPTIONAL_HEADER.SizeOfUninitializedData
		res['AddressOfEntryPoint'] = pe.OPTIONAL_HEADER.AddressOfEntryPoint
		res['BaseOfCode'] = pe.OPTIONAL_HEADER.BaseOfCode
		res['ImageBase'] = pe.OPTIONAL_HEADER.ImageBase
		res['SectionAlignment'] = pe.OPTIONAL_HEADER.SectionAlignment
		res['FileAlignment'] = pe.OPTIONAL_HEADER.FileAlignment
		res['MajorOperatingSystemVersion'] = pe.OPTIONAL_HEADER.MajorOperatingSystemVersion
		res['MinorOperatingSystemVersion'] = pe.OPTIONAL_HEADER.MinorOperatingSystemVersion
		res['MajorImageVersion'] = pe.OPTIONAL_HEADER.MajorImageVersion
		res['MinorImageVersion'] = pe.OPTIONAL_HEADER.MinorImageVersion
		res['MajorSubsystemVersion'] = pe.OPTIONAL_HEADER.MajorSubsystemVersion
		res['MinorSubsystemVersion'] = pe.OPTIONAL_HEADER.MinorSubsystemVersion
		res['SizeOfImage'] = pe.OPTIONAL_HEADER.SizeOfImage
		res['SizeOfHeaders'] = pe.OPTIONAL_HEADER.SizeOfHeaders
		res['CheckSum'] = pe.OPTIONAL_HEADER.CheckSum
		res['Subsystem'] = pe.OPTIONAL_HEADER.Subsystem
		res['DllCharacteristics'] = pe.OPTIONAL_HEADER.DllCharacteristics
		res['SizeOfStackReserve'] = pe.OPTIONAL_HEADER.SizeOfStackReserve
		res['SizeOfStackCommit'] = pe.OPTIONAL_HEADER.SizeOfStackCommit
		res['SizeOfHeapReserve'] = pe.OPTIONAL_HEADER.SizeOfHeapReserve
		res['SizeOfHeapCommit'] = pe.OPTIONAL_HEADER.SizeOfHeapCommit
		res['LoaderFlags'] = pe.OPTIONAL_HEADER.LoaderFlags
		res['NumberOfRvaAndSizes'] = pe.OPTIONAL_HEADER.NumberOfRvaAndSizes
		try: res['BaseOfData'] = pe.OPTIONAL_HEADER.BaseOfData
		except: res['BaseOfData'] = 0


		res['SectionsNb'] = len(pe.sections)
		entropy = list(map(lambda x: x.get_entropy(), pe.sections))
		res['SectionsMeanEntropy'] = sum(entropy) / float(len((entropy)))
		res['SectionsMinEntropy'] = min(entropy)
		res['SectionsMaxEntropy'] = max(entropy)
		raw_sizes = list(map(lambda x: x.SizeOfRawData, pe.sections))
		res['SectionsMeanRawsize'] = sum(raw_sizes) / float(len((raw_sizes)))
		res['SectionsMinRawsize'] = min(raw_sizes)
		res['SectionsMaxRawsize'] = max(raw_sizes)
		virtual_sizes = list(map(lambda x: x.Misc_VirtualSize, pe.sections))
		res['SectionsMeanVirtualsize'] = sum(virtual_sizes) / float(len(virtual_sizes))
		res['SectionsMinVirtualsize'] = min(virtual_sizes)
		res['SectionMaxVirtualsize'] = max(virtual_sizes)

		try:
			res['ImportsNbDLL'] = len(pe.DIRECTORY_ENTRY_IMPORT)
			imports = sum([x.imports for x in pe.DIRECTORY_ENTRY_IMPORT], [])
			res['ImportsNb'] = len(imports)
			res['ImportsNbOrdinal'] = 0
		except:
			res['ImportsNbDLL'] = 0
			res['ImportsNb'] = 0
			res['ImportsNbOrdinal'] = 0

		try: res['ExportNb'] = len(pe.DIRECTORY_ENTRY_EXPORT.symbols)
		except: res['ExportNb'] = 0



		resources = self.get_resources(pe)
		res['ResourcesNb'] = len(resources)
		if len(resources) > 0:
			entropy = list(map(lambda x: x[0], resources))
			res['ResourcesMeanEntropy'] = sum(entropy) / float(len(entropy))
			res['ResourcesMinEntropy'] = min(entropy)
			res['ResourcesMaxEntropy'] = max(entropy)
			sizes = list(map(lambda x: x[1], resources))
			res['ResourcesMeanSize'] = sum(sizes) / float(len(sizes))
			res['ResourcesMinSize'] = min(sizes)
			res['ResourcesMaxSize'] = max(sizes)
		else:
			res['ResourcesNb'] = 0
			res['ResourcesMeanEntropy'] = 0
			res['ResourcesMinEntropy'] = 0
			res['ResourcesMaxEntropy'] = 0
			res['ResourcesMeanSize'] = 0
			res['ResourcesMinSize'] = 0
			res['ResourcesMaxSize'] = 0

		try: res['LoadConfigurationSize'] = pe.DIRECTORY_ENTRY_LOAD_CONFIG.struct.Size
		except AttributeError: res['LoadConfigurationSize'] = 0

		try:
			version_infos = self.get_version_info(pe)
			res['VersionInformationSize'] = len(version_infos.keys())
		except:
			res['VersionInformationSize'] = 0



		pe_features = list(map(lambda x: res[x], features))
		res = clf.predict([pe_features])[0]

		if res == 0: return True
		else: return False


class ScanVirus(ScanVirusAI):

	def __init__(self):
		self.bad_files = []
		self.PE_files = ['exe', 'dll', 'ocx', 'sys', 'scr', 'drv', 'cpl', 'efi', 'acm', 'ax', 'mui', 'tsp']
		self.clf = joblib.load('data/models/classifier.pkl')
		self.features = pickle.loads(open(os.path.join('data/models/features.pkl'), 'rb').read())

	def files_get(self, folder):
		all_paths = []
		for folder_name, sub_folder, filenames in os.walk(folder):
			for f in filenames:
				f = f"{folder_name}/{f}"
				all_paths.append(f)

		return all_paths

	def scanning(self, path):
		if path.split('.')[-1] in self.PE_files:
			if self.extract_infos(path, self.clf, self.features) == True:
				self.bad_files.append(path)
				return

	def scan_all(self, btn, progress_bar, status, path):
		max_threads = 5

		if status == 'folder':
			all_paths = self.files_get(path)
			count_all_paths = len(all_paths)
			count_success_paths = 0

			for file_path in all_paths:
				self.scanning(file_path)
				count_success_paths += 1
				progress_bar.set_value(round(count_success_paths / count_all_paths * 100))

			with DB() as db:
				db.add_virus_storage_info(self.bad_files)

			btn.setEnabled(True)



		elif status == 'file':
			self.scanning(path)






