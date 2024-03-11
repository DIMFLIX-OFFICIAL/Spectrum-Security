import sqlite3, os, requests, datetime, time, threading
from bs4 import BeautifulSoup

class DB(object):
	def __init__(self, db_fp='data/data.db'):
		self.db_fp = db_fp
		self.tables = ["virus_md5_hashes", "processed_virusshare_urls", "programm_settings", "virus_storage"]
		self.connect()
		self.create_tables()
		self.programm_settings()

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		self.conn.commit()
		self.cur.close()
		self.conn.close()

	def __repr__(self):
		return f"<SQLite3 Database: {self.db_fp}>"

	def connect(self):
		self.conn = sqlite3.connect(self.db_fp)
		self.cur = self.conn.cursor()

	def programm_settings(self):
		if not self.exists('Setting', 'programm_settings', 'Language'):
			self.cur.execute("INSERT INTO programm_settings VALUES (?, ?)", ('Language', True))

	def update_programm_settings(self, setting, status):
		self.cur.execute("UPDATE programm_settings SET status = ? WHERE setting = ?", [status, setting])

	def get_programm_settings(self, setting):
		return self.cur.execute("SELECT status FROM programm_settings WHERE setting = ?", [setting,]).fetchone()

	def create_tables(self):
		self.cur.execute('CREATE TABLE IF NOT EXISTS programm_settings(setting TEXT NOT NULL, status BOOLEAN NOT NULL)')
		self.cur.execute('CREATE TABLE IF NOT EXISTS virus_md5_hashes(md5_hash TEXT NOT NULL UNIQUE)')
		self.cur.execute('CREATE TABLE IF NOT EXISTS processed_virusshare_urls(url TEXT NOT NULL UNIQUE)')
		self.cur.execute('CREATE TABLE IF NOT EXISTS virus_storage(date TEXT NOT NULL, path TEXT NOT NULL PRIMARY KEY)')
		self.conn.commit()

	def exists(self, vname, table, value):
		sql = f"SELECT {vname} FROM {table} WHERE {vname} = (?)"
		self.cur.execute(sql, (value,))
		return self.cur.fetchone() is not None

	def reset(self):
		self.close()
		os.remove(self.db_fp)
		self.connect()
		self.update()

	def add(self, table, value):
		if table not in self.tables:
			raise ValueError("This table does not exist")
		sql = f"INSERT OR IGNORE INTO {table} VALUES (?)"
		self.cur.execute(sql, (value,))

	def add_multiple(self, table, values):
		if table not in self.tables:
			raise ValueError("This table does not exist")
		sql = f"INSERT OR IGNORE INTO {table} VALUES (?)"
		self.cur.executemany(sql, [(value,) for value in values])

	def update(self, max_threads=5):
		urls = self.get_virusshare_urls()
		total = len(urls)
		count = 0

		try:
			while True:
				if threading.active_count() < max_threads:
					self.update_md5_hashes(urls[0])
					urls.pop(0)
					count += 1
					print(f'Scanning Files - Threads: {threading.active_count()} Total: {total}	Updated: {count}')
				else:
					time.sleep(0.01)
		except:
			input('Press ENTER please: ')
			os.system('cls')

	def update_md5_hashes(self, url):
		if not self.exists('url', 'processed_virusshare_urls', url):
			self.add_multiple('virus_md5_hashes', self.get_virusshare_hashes(url))
			self.add('processed_virusshare_urls', url)
			self.conn.commit()


	def get_virusshare_urls(self):
		r = requests.get('https://virusshare.com/hashes.4n6')
		soup = BeautifulSoup(r.content, 'html.parser')
		return [f"https://virusshare.com/{a['href']}" for a in soup.find_all('a')][6:-2]

	def get_virusshare_hashes(self, url):
		r = requests.get(url)
		return r.text.splitlines()[6:]







	def delete_virus_storage_info(self, virus):
		try: self.cur.execute("DELETE FROM virus_storage WHERE path=?", [virus])
		except Exception as er: print(er)

	def add_virus_storage_info(self, viruses, date=None):

		if date == None:
			date = datetime.datetime.now()
			date = date.strftime("%d-%m-%Y %H:%M")

		if type(viruses) == list:
			for virus in viruses:
				self.cur.execute("INSERT OR IGNORE INTO virus_storage VALUES(?, ?)", [str(date), virus])
		else:
			self.cur.execute("INSERT OR IGNORE INTO virus_storage VALUES(?, ?)", [str(date), viruses])

	def get_virus_storage_info(self):
		data = self.cur.execute("SELECT * FROM virus_storage").fetchall()
		list_of_lists = [list(elem) for elem in data]
		return list_of_lists