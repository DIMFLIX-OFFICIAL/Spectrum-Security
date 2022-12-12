
##==> IMPORT LIBRARIES
####################################################
import sys, psutil, GPUtil, easygui, threading
from winreg import *
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtMultimedia import QSound
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

##==> IMPORT UI FILES
####################################################
from ui import rc_resource
from ui.spectrum_ui_main import Ui_MainWindow as SpectrumSecurityWindow
from ui.spectrum_ui_notify import Ui_MainWindow as SpectrumSecurityNotify
from ui.widgets.circular_progress import CicularProgress
from ui.widgets.toggleswitch import ToggleSwitch

##==> IMPORT OTHER PARTS OF PROJECT
####################################################
from db import DB
from antivirus import ScanVirus










##==> MAIN INTERFACE CLASS
####################################################
class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = SpectrumSecurityWindow()
		self.ui.setupUi(self)

		tray_icon = SystemTrayIcon(QIcon("ui\designer\imgs\general\icon.png"), self)
		tray_icon.show()

		##==> WINDOW OPTIONS
		####################################################
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

		##==> WINDOW BUTTONS
		####################################################
		self.ui.top_menu_minimize_btn.clicked.connect(lambda: self.showMinimized())
		self.ui.top_menu_close_btn.clicked.connect(lambda: self.close())


		##==> EVENTS
		####################################################
		self.ui.top_menu_header.mouseMoveEvent = self.moveWindow

		self.ui.bottom_menu_scroll_area.installEventFilter(self)

		self.ui.bottom_menu_home.installEventFilter(self)
		self.ui.bottom_menu_scanning.installEventFilter(self)
		self.ui.bottom_menu_virus_storage.installEventFilter(self)
		self.ui.bottom_menu_faq.installEventFilter(self)
		self.ui.bottom_menu_settings.installEventFilter(self)

		self.ui.home_secret_way.installEventFilter(self)
		self.ui.scanning_secret_way.installEventFilter(self)
		self.ui.faq_secret_way.installEventFilter(self)
		self.ui.settings_secret_way.installEventFilter(self)


		##==> START WIDGET SETTINGS ON PAGES
		####################################################
		self.home_page_widgets_settings()
		self.scanning_page_widgets_settings()
		self.virus_storage_page_widgets_settings()
		self.faq_page_widgets_settings()
		self.settings_page_widgets_settings()


		self.show()





	##==> HOME PAGE WIDGETS SETTINGS
	####################################################
	def home_page_widgets_settings(self):

		##==> UPDATING INFORMATION ON HOME PAGE
		####################################################
		self.home_timer_update = QTimer(self)
		self.home_timer_update.timeout.connect(lambda: self.main_page_info())
		self.home_timer_update.start(1000)

	def get_cpu_name(self):
		aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
		aKey = OpenKey(aReg, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
		name = QueryValueEx(aKey, 'ProcessorNameString')[0]
		return name

	def main_page_info(self):

		gpus = GPUtil.getGPUs()


		with DB() as db:
			lang = bool(db.get_programm_settings('Language')[0])

		self.ui.CPU_progress.setText(f'CPU - {round(psutil.cpu_percent())}%')
		self.ui.RAM_progress.setText(f'RAM - {round(psutil.virtual_memory().percent)}%')


		if lang:
			self.ui.CPU_info.setText(f"Model - {self.get_cpu_name()}")
			self.ui.Physical_cores_info.setText(f'Physical cores - {psutil.cpu_count(logical=True)}')
			self.ui.Frequency_info.setText(f'Frequency - {psutil.cpu_freq().current:.2f}MHz')

			self.ui.RAM_total_info.setText(f'Total - {round(psutil.virtual_memory().total/1000000000, 2)}GB')
			self.ui.RAM_used_info.setText(f'Used - {round(psutil.virtual_memory().used/1000000000, 2)}GB')

			if gpus != []:
				self.ui.GPU_progress.setText(f'GPU - {gpus[0].load*100}%')
				self.ui.GPU_model_info.setText(f'Model - {gpus[0].name}')
				self.ui.GPU_vram_total_info.setText(f'Total VRAM - {gpus[0].memoryTotal}')
				self.ui.GPU_vram_used_info.setText(f'Used VRAM - {gpus[0].memoryUsed}')
			else:
				self.ui.GPU_progress.setText(f'GPU - 0%')
				self.ui.GPU_model_info.setText(f'Model - Not Found')
				self.ui.GPU_vram_total_info.setText(f'Total VRAM - 0.0MB')
				self.ui.GPU_vram_used_info.setText(f'Used VRAM - 0.0MB')

		else:
			self.ui.CPU_info.setText(f"Модель - {self.get_cpu_name()}")
			self.ui.Physical_cores_info.setText(f'Физические ядра - {psutil.cpu_count(logical=True)}')
			self.ui.Frequency_info.setText(f'Частота - {psutil.cpu_freq().current:.2f}MHz')

			self.ui.RAM_total_info.setText(f'Общая - {round(psutil.virtual_memory().total / 1000000000, 2)}GB')
			self.ui.RAM_used_info.setText(f'Использованная - {round(psutil.virtual_memory().used / 1000000000, 2)}GB')

			if gpus != []:
				self.ui.GPU_progress.setText(f'GPU - {gpus[0].load * 100}%')
				self.ui.GPU_model_info.setText(f'Модель - {gpus[0].name}')
				self.ui.GPU_vram_total_info.setText(f'Общая VRAM - {gpus[0].memoryTotal}')
				self.ui.GPU_vram_used_info.setText(f'Использованная VRAM - {gpus[0].memoryUsed}')
			else:
				self.ui.GPU_progress.setText(f'GPU - 0%')
				self.ui.GPU_model_info.setText(f'Модель - Not Found')
				self.ui.GPU_vram_total_info.setText(f'Общая VRAM - 0.0MB')
				self.ui.GPU_vram_used_info.setText(f'Использованная VRAM - 0.0MB')


	##==> SCAN PAGE WIDGETS SETTINGS
	####################################################
	def scanning_page_widgets_settings(self):
		self.progress_bar_scan = CicularProgress()
		self.progress_bar_scan.value = 0
		self.ui.scanning_progress_bar_widget.addWidget(self.progress_bar_scan)
		self.ui.scanning_start_btn.clicked.connect(lambda: self.scan_btn_start())

	def scan_btn_start(self):
		self.ui.scanning_start_btn.setEnabled(False)
		full = self.ui.scanning_choose_btn_full.isChecked()
		folder = self.ui.scanning_choose_btn_folder.isChecked()
		file = self.ui.scanning_choose_btn_file.isChecked()

		if full:
			path = 'C:/'
			status = 'folder'

		elif folder:
			path = easygui.diropenbox()
			status = 'folder'
		elif file:
			path = easygui.fileopenbox(default="*.exe", filetypes = ['*.exe', '*.dll', '*.ocx', '*.sys', '*.scr', '*.drv', '*.cpl', '*.efi', '*.acm', '*.ax', '*.mui', '*.tsp'])
			status = 'file'
		else:
			path = None
			status = None


		if path != None:
			self.progress_bar_scan.set_value(0)
			scan_class = ScanVirus()
			threading.Thread(target=scan_class.scan_all, args=(self.ui.scanning_start_btn, self.progress_bar_scan, status, path)).start()

			if status == 'file':
				self.scanning_progress_timer = QtCore.QTimer()
				self.scanning_progress_timer.timeout.connect(self.circular_progress_adding)
				self.scanning_progress_timer.start(0.025)

		else:
			self.ui.scanning_start_btn.setEnabled(True)



	def circular_progress_adding(self):
		self.progress_bar_scan.set_value(self.progress_bar_scan.value + 1)

		if self.progress_bar_scan.value == 100:
			self.scanning_progress_timer.stop()
			self.ui.scanning_start_btn.setEnabled(True)


	##==> STORAGE PAGE WIDGETS SETTINGS
	####################################################
	def virus_storage_page_widgets_settings(self):
		self.ui.virus_storage_table.setColumnWidth(0, 135)
		self.ui.virus_storage_table.setColumnWidth(1, 87)
		self.ui.virus_storage_table.setColumnWidth(2, 480)
		self.ui.virus_storage_table.setColumnWidth(3, 40)
		self.ui.virus_storage_table.setColumnWidth(4, 40)
		self.ui.virus_storage_table.setColumnWidth(5, 40)

		self.virus_storage_update_info('start_update')

		self.virus_storage_timer_update = QTimer(self)
		self.virus_storage_timer_update.timeout.connect(lambda: self.virus_storage_update_info('constant_update'))
		self.virus_storage_timer_update.start(1000)

	def virus_storage_update_info(self, state):

		with DB() as db:
			data_from_sql = db.get_virus_storage_info()

		if state == 'start_update':
			self.ui.virus_storage_table.clear()
			self.ui.virus_storage_table.setRowCount(0)

			for i in data_from_sql:
				self.virus_storage_table_add(i[1], i[0])

		elif state == 'constant_update':
			# СБОР ИНФОРМАЦИИ ИЗ ТАБЛИЦЫ
			rows = self.ui.virus_storage_table.rowCount()
			data_from_table = []
			for row in range(rows):
				tmp = []
				tmp.append(self.ui.virus_storage_table.item(row, 0).text())
				tmp.append(self.ui.virus_storage_table.item(row, 2).text())
				data_from_table.append(tmp)

			if data_from_table != data_from_sql:
				self.ui.virus_storage_table.clear()
				self.ui.virus_storage_table.setRowCount(0)

				for i in data_from_sql:
					self.virus_storage_table_add(i[1], i[0])

	def virus_storage_table_add(self, path, date=None):

		close_btn = QPushButton()
		close_btn.clicked.connect(self.virus_storage_table_close_btn)
		close_btn.setStyleSheet("background: none;")
		icon_btn_close = QIcon()
		icon_btn_close.addFile(u":/general/imgs/general/close.png", QSize(18, 18), QIcon.Normal, QIcon.Off)
		close_btn.setIcon(icon_btn_close)
		close_btn.setMaximumSize(QSize(30, 30))

		delete_btn = QPushButton()
		delete_btn.clicked.connect(self.virus_storage_table_delete_btn)
		delete_btn.setStyleSheet("background: none;")
		icon_btn_del = QIcon()
		icon_btn_del.addFile(u":/general/imgs/general/trash.png", QSize(18, 18), QIcon.Normal, QIcon.Off)
		delete_btn.setIcon(icon_btn_del)
		delete_btn.setMaximumSize(QSize(30, 30))

		copy_btn = QPushButton()
		copy_btn.clicked.connect(self.virus_storage_table_copy_btn)
		copy_btn.setStyleSheet("background: none;")
		icon_btn_copy = QIcon()
		icon_btn_copy.addFile(u":/general/imgs/general/copy.png", QSize(18, 18), QIcon.Normal, QIcon.Off)
		copy_btn.setIcon(icon_btn_copy)
		copy_btn.setMaximumSize(QSize(30, 30))

		rowPosition = self.ui.virus_storage_table.rowCount()
		self.ui.virus_storage_table.insertRow(rowPosition)
		self.ui.virus_storage_table.setRowHeight(rowPosition, 30)

		if date == None:
			date = datetime.datetime.now()
			date = date.strftime("%d-%m-%Y %H:%M")

		self.ui.virus_storage_table.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(date)))
		self.ui.virus_storage_table.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem('|  Malware - '))
		self.ui.virus_storage_table.setItem(rowPosition, 2,QtWidgets.QTableWidgetItem(path))
		self.ui.virus_storage_table.setCellWidget(rowPosition, 3, copy_btn)
		self.ui.virus_storage_table.setCellWidget(rowPosition, 4, delete_btn)
		self.ui.virus_storage_table.setCellWidget(rowPosition, 5, close_btn)

		with DB() as db:
			db.add_virus_storage_info([path], date)

	def virus_storage_table_close_btn(self):
		button = self.sender()
		row = self.ui.virus_storage_table.indexAt(button.pos()).row()
		path = self.ui.virus_storage_table.item(row, 2).text()
		self.ui.virus_storage_table.removeRow(row)
		with DB() as db:
			db.delete_virus_storage_info(path)

	def virus_storage_table_delete_btn(self):
		button = self.sender()
		row = self.ui.virus_storage_table.indexAt(button.pos()).row()
		path = self.ui.virus_storage_table.item(row, 2).text()

		if os.path.exists(path):
			os.remove(path)
			self.ui.virus_storage_table.removeRow(row)
		else:
			self.ui.virus_storage_table.removeRow(row)

		with DB() as db:
			db.delete_virus_storage_info(path)

	def virus_storage_table_copy_btn(self):
		button = self.sender()
		row = self.ui.virus_storage_table.indexAt(button.pos()).row()
		pyperclip.copy(self.ui.virus_storage_table.item(row, 2).text())





	##==> FAQ PAGE WIDGETS SETTINGS
	####################################################
	def faq_page_widgets_settings(self):

		with DB() as db:
			lang = db.get_programm_settings('Language')[0]

		if lang == 1:
			self.ui.faq_small_description_btn.clicked.connect(lambda: self.open_dropdown_menu_animation(self.ui.faq_small_description_btn,self.ui.faq_small_description_white_background, 34, 105))

			self.ui.faq_home_page_btn.clicked.connect(lambda: self.open_dropdown_menu_animation(self.ui.faq_home_page_btn, self.ui.faq_home_page_white_background, 34, 90))
			self.ui.faq_scan_page_btn.clicked.connect(lambda: self.open_dropdown_menu_animation(self.ui.faq_scan_page_btn, self.ui.faq_scan_page_white_background, 34, 175))
			self.ui.faq_virus_storage_page_btn.clicked.connect(lambda: self.open_dropdown_menu_animation(self.ui.faq_virus_storage_page_btn, self.ui.faq_virus_storage_page_white_background, 34, 155))
			self.ui.faq_faq_page_btn.clicked.connect(lambda: self.open_dropdown_menu_animation(self.ui.faq_faq_page_btn, self.ui.faq_faq_page_white_background,34, 90))
			self.ui.faq_settings_page_btn.clicked.connect(lambda: self.open_dropdown_menu_animation(self.ui.faq_settings_page_btn, self.ui.faq_settings_page_white_background, 34, 70))

			self.ui.faq_authors_btn.clicked.connect(lambda: self.open_dropdown_menu_animation(self.ui.faq_authors_btn, self.ui.faq_authors_white_background,34, 125))

		else:
			self.ui.faq_small_description_btn.clicked.connect(lambda: self.open_dropdown_menu_animation(self.ui.faq_small_description_btn, self.ui.faq_small_description_white_background, 34, 119))

			self.ui.faq_home_page_btn.clicked.connect(lambda: self.open_dropdown_menu_animation(self.ui.faq_home_page_btn, self.ui.faq_home_page_white_background, 34,90))
			self.ui.faq_scan_page_btn.clicked.connect(lambda: self.open_dropdown_menu_animation(self.ui.faq_scan_page_btn, self.ui.faq_scan_page_white_background,34, 190))
			self.ui.faq_virus_storage_page_btn.clicked.connect(lambda: self.open_dropdown_menu_animation(self.ui.faq_virus_storage_page_btn, self.ui.faq_virus_storage_page_white_background,34, 155))
			self.ui.faq_faq_page_btn.clicked.connect(lambda: self.open_dropdown_menu_animation(self.ui.faq_faq_page_btn, self.ui.faq_faq_page_white_background,34, 105))
			self.ui.faq_settings_page_btn.clicked.connect(lambda: self.open_dropdown_menu_animation(self.ui.faq_settings_page_btn, self.ui.faq_settings_page_white_background,34, 90))

			self.ui.faq_authors_btn.clicked.connect(lambda: self.open_dropdown_menu_animation(self.ui.faq_authors_btn, self.ui.faq_authors_white_background, 34, 125))

		self.close_all_dropdown_menus()




	##==> SETTINGS PAGE WIDGETS SETTINGS
	####################################################
	def settings_page_widgets_settings(self):

		## ==> DROPDOWN MENU BTNS
		##############################################################
		self.ui.settings_lang_btn.clicked.connect(lambda: self.open_dropdown_menu_animation(self.ui.settings_lang_btn, self.ui.settings_lang_white, 35, 95))

		## ==> LANGUAGE
		##############################################################
		self.ui.settings_lang_eng_frame.installEventFilter(self)
		self.ui.settings_lang_rus_frame.installEventFilter(self)

		with DB() as db:
			status = bool(db.get_programm_settings('Language')[0])

		if status == False:
			self.ui.settings_lang_eng_icon.hide()
			self.ui.settings_lang_title.setText(f'Язык: Русский')
			self.change_lang_rus()

		elif status == True:
			self.ui.settings_lang_rus_icon.hide()
			self.ui.settings_lang_title.setText(f'Language: English')






	##==> ANIMATIONS
	####################################################
	def open_dropdown_menu_animation(self, button, object, standart_h, end_h):
		current_h = object.minimumHeight()

		if current_h == standart_h:
			animation = QPropertyAnimation(object, b"maximumHeight")
			animation.setDuration(100)
			animation.setEndValue(end_h)

			animation1 = QPropertyAnimation(object, b"minimumHeight")
			animation1.setDuration(100)
			animation1.setEndValue(end_h)

			up_arrow_icon = QIcon()
			up_arrow_icon.addFile(u":/general/imgs/general/up_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
			button.setIcon(up_arrow_icon)

			group = QParallelAnimationGroup(self)
			group.addAnimation(animation)
			group.addAnimation(animation1)
			group.start()

		elif current_h == end_h:
			animation = QPropertyAnimation(object, b"maximumHeight")
			animation.setDuration(100)
			animation.setEndValue(standart_h)

			animation1 = QPropertyAnimation(object, b"minimumHeight")
			animation1.setDuration(100)
			animation1.setEndValue(standart_h)

			down_arrow_icon = QIcon()
			down_arrow_icon.addFile(u":/general/imgs/general/down_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
			button.setIcon(down_arrow_icon)

			group = QParallelAnimationGroup(self)
			group.addAnimation(animation)
			group.addAnimation(animation1)
			group.start()

	def close_all_dropdown_menus(self):

		faq_list = [
			(self.ui.faq_small_description_white_background, self.ui.faq_small_description_btn),
			(self.ui.faq_home_page_white_background, self.ui.faq_home_page_btn),
			(self.ui.faq_scan_page_white_background, self.ui.faq_scan_page_btn),
			(self.ui.faq_virus_storage_page_white_background, self.ui.faq_virus_storage_page_btn),
			(self.ui.faq_faq_page_white_background, self.ui.faq_faq_page_btn),
			(self.ui.faq_settings_page_white_background, self.ui.faq_settings_page_btn),
			(self.ui.faq_authors_white_background, self.ui.faq_authors_btn)
		]

		for element in faq_list:
			element[0].setMinimumSize(470, 34)
			element[0].setMaximumSize(470, 34)
			down_arrow_icon = QIcon()
			down_arrow_icon.addFile(u":/general/imgs/general/down_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
			element[1].setIcon(down_arrow_icon)



	##==> EVENT FILTER
	###########################################################
	def eventFilter(self, obj, e):
		try:

			## ==> BOTTOM_MENU_WHEEL_EVENT
			###########################################################
			if obj == self.ui.bottom_menu_scroll_area and e.type() == 31:
				self.ui.bottom_menu_scroll_area.horizontalScrollBar().wheelEvent(e)


			## ==> PAGE SWITCHING
			###########################################################
			elif obj == self.ui.bottom_menu_home and e.type() == 2: self.ui.Pages.setCurrentWidget(self.ui.HomePage)
			elif obj == self.ui.bottom_menu_scanning and e.type() == 2: self.ui.Pages.setCurrentWidget(self.ui.ScanningPage)
			elif obj == self.ui.bottom_menu_virus_storage and e.type() == 2: self.ui.Pages.setCurrentWidget(self.ui.VirusStoragePage)
			elif obj == self.ui.bottom_menu_faq and e.type() == 2: self.ui.Pages.setCurrentWidget(self.ui.FaqPage)
			elif obj == self.ui.bottom_menu_settings and e.type() == 2: self.ui.Pages.setCurrentWidget(self.ui.SettingsPage)


			## ==> LANGUAGES CHOOSING
			###########################################################
			elif obj == self.ui.settings_lang_rus_frame and e.type() == 2:
				with DB() as db: db.update_programm_settings("Language", False)
				self.ui.settings_lang_title.setText('Язык: Русский')
				self.ui.settings_lang_eng_icon.hide()
				self.ui.settings_lang_rus_icon.show()
				self.change_lang_rus()


			elif obj == self.ui.settings_lang_eng_frame and e.type() == 2:
				with DB() as db: db.update_programm_settings("Language", True)
				self.ui.settings_lang_title.setText('Language: English')
				self.ui.settings_lang_rus_icon.hide()
				self.ui.settings_lang_eng_icon.show()
				self.change_lang_eng()



			## ==> SECRET WAYS
			###########################################################
			elif (obj == self.ui.home_secret_way or obj == self.ui.scanning_secret_way or obj == self.ui.faq_secret_way or obj == self.ui.settings_secret_way) and e.type() == 2:

				with DB() as db:
					lang = bool(db.get_programm_settings('Language')[0])

				if lang == False:
					self.notify = Notify(text="<b>Я люблю ваш компьютер и данные хранящиеся на нем :3</b>")

				elif lang == True:
					self.notify = Notify(text="<b>I Love your computer and the data stored on it :3</b>")




		except Exception as er: print(er)
		return super(QMainWindow, self).eventFilter(obj, e)


	##==> MOVING THE PROGRAM
	####################################################
	def moveWindow(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()

	def mousePressEvent(self, event):
		self.dragPos = event.globalPos()


	##==> CHANGE LANG
	####################################################
	def change_lang_rus(self):

		##==> СТРАНИЦА СКАНИРОВАНИЯ
		####################################################
		self.ui.scanning_choose_btn_full.setText("Полная")
		self.ui.scanning_choose_btn_folder.setText("Папка")
		self.ui.scanning_choose_btn_file.setText("Файл")
		self.ui.scanning_start_btn.setText("СКАНИРОВАТЬ")

		self.ui.scanning_choose_btn_full.setStyleSheet(self.ui.scanning_choose_btn_full.styleSheet().replace('width: 35px;', 'width: 23px;'))
		self.ui.scanning_choose_btn_folder.setStyleSheet(self.ui.scanning_choose_btn_folder.styleSheet().replace('width: 22px;', 'width: 28px;'))
		self.ui.scanning_choose_btn_file.setStyleSheet(self.ui.scanning_choose_btn_file.styleSheet().replace('width: 37px;', 'width: 32px;'))



		##==> СТРАНИЦА FAQ
		####################################################
		self.ui.faq_small_description_title.setText("Маленькое описание")
		self.ui.faq_small_description_text.setText("<html><head/><body><p>Spectrum Security - это начинающий проект, который быстро набирает обороты.  У нас есть довольно большая база данных вирусов, в количестве 30 миллионов, а также наш собственный искусственный интеллект, который может обнаружить любое вредоносное ПО.</p></body></html>")

		self.ui.faq_home_page_title.setText("Домашняя страница")
		self.ui.faq_home_page_text.setText("<html><head/><body><p>Домашняя страница, или же Главная страница, отвечает за вывод информации о нагрузке вашего ПК. В ней представлены самые главные параметры, а именно нагрузка CPU, RAM и GPU.</p></body></html>")

		self.ui.faq_scan_page_title.setText("Сканирование")
		self.ui.faq_scan_page_text.setText("<html><head/><body><p>В вкладке сканирования сверху нас встречает небольшое меню, состоящее из 3 кнопок: Полная, Папка и Файл. Оно отвечает за выбор режима сканирования. Полная - проверка всего вашего компьютера на наличие вирусов. Папка - проверка выбранной вами папки. Файл - проверка выбранного вами файла. Чуть ниже данного меню находится круговой индикатор выполнения процесса сканирования. В самом низу расположена кнопка \"Сканировать\" после нажатия на которую будет произведено сканирование в выбранном вами режиме.</p></body></html>")

		self.ui.faq_virus_storage_page_title.setText("Хранилище вирусов")
		self.ui.faq_virus_storage_page_text.setText("<html><head/><body><p>Вкладка Хранилище отвечает за хранение и взаимодействие с найденными вирусами. В строке с найденной  угрозой будет представлена информация: дата сканирования, тип угрозы и путь до вредоносного файла. Так же присутствуют три кнопки, первая отвечает за копирование пути к файлу, вторая за удаление зараженного файла, а третья за убирание его из списка найденных угроз.</p></body></html>")

		self.ui.faq_faq_page_title.setText("Страница FAQ")
		self.ui.faq_faq_page_text.setText("<html><head/><body><p>В вкладке FAQ, в которой вы собственно сейчас и находитесь, представлены различные инструкции и ответы на интересующие вас вопросы. В процессе обновлений библиотека FAQ будет стремительно расширяться.</p></body></html>")

		self.ui.faq_settings_page_title.setText("Настройки")
		self.ui.faq_settings_page_text.setText("<html><head/><body><p>Вкладка Настройки отвечает за гибкое изменение различных параметров программы, для улучшения её работоспособности.</p></body></html>")

		self.ui.faq_authors_title.setText("Авторы")
		self.ui.faq_authors_text.setText("<html><head/><body><p>Разработчик - DIMFLIX</p><p>UX/UI Дизайнер и Разработчик - DIMFLIX </p><p>Логотип и имя компании - PlayStack</body></html>")

		self.faq_page_widgets_settings()

		##==> НАСТРОЙКИ
		####################################################
		self.ui.settings_lang_rus_title.setText("Русский")
		self.ui.settings_lang_eng_title.setText("English")



		##==> ХРАНИЛИЩЕ ВИРУСОВ
		####################################################
		font = QFont()
		font.setFamily(u"Segoe UI")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.ui.virus_storage_main_title_label.setText("ХРАНИЛИЩЕ ВИРУСОВ")
		self.ui.virus_storage_warning.setText("Предупреждение - антивирус находится в стадии разработки, что может привести к неточным определениям вирусов.  Огромная просьба проверить файл самостоятельно, дабы избежать удаления ценной информации или системных файлов.")
		self.ui.virus_storage_warning.setFont(font)



		##==> НИЖНЯЯ ПАНЕЛЬ
		####################################################
		self.ui.home_title.setText("Главная")
		self.ui.home_description.setText("Просмотр производительности")

		self.ui.scanning_title.setText("Сканирование")
		self.ui.scanning_description.setText("Сканирование ПК на вирусы")

		self.ui.virus_storage_title.setText("Хранилище")
		self.ui.virus_storage_description.setText("Хранилище найденных вирусов")

		self.ui.faq_title.setText("FAQ")
		self.ui.faq_description.setText("Часто задаваемые вопросы")

		self.ui.settings_title.setText("Настройки")
		self.ui.settings_description.setText("Настройки программы")

	def change_lang_eng(self):

		##==> СТРАНИЦА СКАНИРОВАНИЯ
		####################################################
		self.ui.scanning_choose_btn_full.setText("FULL")
		self.ui.scanning_choose_btn_folder.setText("FOLDER")
		self.ui.scanning_choose_btn_file.setText("FILE")
		self.ui.scanning_start_btn.setText("SCAN")

		self.ui.scanning_choose_btn_full.setStyleSheet(self.ui.scanning_choose_btn_full.styleSheet().replace('width: 23px;', 'width: 35px;'))
		self.ui.scanning_choose_btn_folder.setStyleSheet(self.ui.scanning_choose_btn_folder.styleSheet().replace('width: 28px;', 'width: 22px;'))
		self.ui.scanning_choose_btn_file.setStyleSheet(self.ui.scanning_choose_btn_file.styleSheet().replace('width: 32px;', 'width: 37px;'))





		##==> СТРАНИЦА FAQ
		####################################################
		self.ui.faq_small_description_title.setText("Small description")
		self.ui.faq_small_description_text.setText("<html><head/><body><p>Spectrum Security is a start-up project that is rapidly gaining momentum.  We have a fairly large database of viruses, in the amount of 30 million, as well as our own artificial intelligence that can detect any malware.</p></body></html>")

		self.ui.faq_home_page_title.setText("Home Page")
		self.ui.faq_home_page_text.setText("<html><head/><body><p>The Home page, or the Main page, is responsible for displaying information about the load of your PC. It presents the most important parameters, namely the CPU, RAM and GPU load.</p></body></html>")

		self.ui.faq_scan_page_title.setText("Scanning Page")
		self.ui.faq_scan_page_text.setText("<html><head/><body><p>In the scan tab on top we are greeted by a small menu consisting of 3 buttons: Full, Folder and File. It is responsible for selecting the scanning mode. Full - scan of your entire computer for viruses. Folder - checking the folder you selected. File - checking the file you selected. Just below this menu is a circular indicator of the scanning process. At the very bottom there is a &quot;Scan&quot; button, after clicking on which a scan will be performed in the mode you selected.</p></body></html>")

		self.ui.faq_virus_storage_page_title.setText("Virus Storage Page")
		self.ui.faq_virus_storage_page_text.setText("<html><head/><body><p>The Storage tab is responsible for storing and interacting with found viruses. The line with the found threat will contain information: the date of the scan, the type of threat and the path to the malicious file. There are also three buttons, the first is responsible for copying the path to the file, the second for deleting the infected file, and the third for removing it from the list of threats found.</p></body></html>")

		self.ui.faq_faq_page_title.setText("FAQ Page")
		self.ui.faq_faq_page_text.setText("<html><head/><body><p>The FAQ tab, in which you are actually now, provides various instructions and answers to your questions. In the process of updates, the FAQ library will expand rapidly.</p></body></html>")

		self.ui.faq_settings_page_title.setText("Settings Page")
		self.ui.faq_settings_page_text.setText("<html><head/><body><p>The Settings tab is responsible for flexibly changing various program parameters to improve its performance.</p></body></html>")

		self.ui.faq_authors_title.setText("Authors")
		self.ui.faq_authors_text.setText("<html><head/><body><p>Developer - DIMFLIX</p><p>UX/UI Designer and Developer - DIMFLIX </p><p>Logo and Company name- PlayStack </p></body></html>")

		self.faq_page_widgets_settings()


		##==> ХРАНИЛИЩЕ ВИРУСОВ
		####################################################
		font = QFont()
		font.setFamily(u"Segoe UI")
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.ui.virus_storage_main_title_label.setText("VIRUS STORAGE")
		self.ui.virus_storage_warning.setText("<html><head/><body><p>Warning - the antivirus is under development, which may cause inaccurate virus definitions.  A huge request to check the file yourself, in order to avoid deleting valuable information or system files</p></body></html>")
		self.ui.virus_storage_warning.setFont(font)


		##==> НИЖНЯЯ ПАНЕЛЬ
		####################################################
		self.ui.home_title.setText("Home Page")
		self.ui.home_description.setText("PC performance monitoring")

		self.ui.scanning_title.setText("Scanning")
		self.ui.scanning_description.setText("Scan your PC for viruses")

		self.ui.virus_storage_title.setText("Virus storage")
		self.ui.virus_storage_description.setText("Storage of found viruses")

		self.ui.faq_title.setText("FAQ")
		self.ui.faq_description.setText("Frequently asked questions")

		self.ui.settings_title.setText("Settings")
		self.ui.settings_description.setText("Application Settings")











##==> NOTIFY INTERFACE CLASS
####################################################
class Notify(QMainWindow):
	def __init__(self, text):
		QMainWindow.__init__(self)
		self.ui = SpectrumSecurityNotify()
		self.ui.setupUi(self)

		## ==> MAIN SETTINGS
		##############################################################
		self.setWindowFlags(Qt.ToolTip)
		self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

		self.ui.notify_text.setText(text)

		## ==> WINDOW BTNS
		##############################################################
		self.ui.close_btn.clicked.connect(lambda: self.close_notify())

		## ==> MOVE TO BOTTOM RIGHT
		##############################################################
		self.desktop = QGuiApplication.primaryScreen().availableGeometry()
		self.start_animation()

		self.notify = QSound('data/notifications/notification.wav', self)
		self.notify.play()

		self.show()

	def start_animation(self):
		self.start_animation = QPropertyAnimation(self, b"geometry")
		self.start_animation.setDuration(200)
		self.start_animation.setStartValue(QRect(self.desktop.width() - 1, self.desktop.height() - 110, 1, 100))
		self.start_animation.setEndValue(QRect(self.desktop.width() - 410, self.desktop.height() - 110, 400, 100))
		self.start_animation.start()
		QTimer.singleShot(5200, lambda: self.end_animation())

	def end_animation(self):
		self.end_animation = QPropertyAnimation(self, b"geometry")
		self.end_animation.setDuration(200)
		self.end_animation.setStartValue(QRect(self.desktop.width() - 410, self.desktop.height() - 110, 400, 100))
		self.end_animation.setEndValue(QRect(self.desktop.width() - 1, self.desktop.height() - 110, 1, 100))
		self.end_animation.start()
		QTimer.singleShot(200, lambda: self.close_notify())

	def close_notify(self):
		self.close()


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

	def __init__(self, icon, parent=None):
		QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
		self.setToolTip(f'Spectrum Security')
		menu = QtWidgets.QMenu(parent)

		menu.addAction(QtGui.QIcon("icons/exit.png"), "Выйти", lambda: sys.exit())
		menu.addSeparator()
		self.setContextMenu(menu)
		self.activated.connect(self.onTrayIconActivated)

	def onTrayIconActivated(self, event):
		if event == self.Trigger:  # при одиночном клике ЛЕВОЙ КНОПКОЙ МЫШИ - показывает МЕНЮ
			self.contextMenu().exec_(QtGui.QCursor.pos())  # показывает меню в текущей позиции мыши





if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())