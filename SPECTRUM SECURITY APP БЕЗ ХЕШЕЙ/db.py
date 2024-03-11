import sqlite3, os, datetime

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

	def create_tables(self):
		self.cur.execute('CREATE TABLE IF NOT EXISTS programm_settings(setting TEXT NOT NULL, status BOOLEAN NOT NULL)')
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







	def programm_settings(self):
		if not self.exists('Setting', 'programm_settings', 'Language'):
			self.cur.execute("INSERT INTO programm_settings VALUES (?, ?)", ('Language', True))

	def update_programm_settings(self, setting, status):
		self.cur.execute("UPDATE programm_settings SET status = ? WHERE setting = ?", [status, setting])

	def get_programm_settings(self, setting):
		return self.cur.execute("SELECT status FROM programm_settings WHERE setting = ?", [setting,]).fetchone()







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