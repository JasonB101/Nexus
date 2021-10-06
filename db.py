import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS settings (id INTEGER PRIMARY KEY, gcode_file_path text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS profiles (id INTEGER PRIMARY KEY, filename text, power int, speed int)")
        self.conn.commit()

        #Need to create a model for the burning profile. (Filename linked to speed and power)

    def defaultGcodePathFetch(self):
        self.cur.execute("SELECT * FROM settings")
        defaultPath = self.cur.fetchone()
        return defaultPath
    
    def fetchProfile(self, filename):
        self.cur.execute("SELECT * FROM profiles WHERE filename= ?", (filename,))
        profile = self.cur.fetchone()
        return profile
        
    def insertSettings(self, path):
        self.cur.execute("INSERT INTO settings VALUES (77, ?)", (path,))
        self.conn.commit()

    def removeSettings(self, id):
        self.cur.execute("DELETE FROM settings WHERE id=?", (id,))
        self.conn.commit()

    def updateSettings(self, id, path):
        self.cur.execute("UPDATE settings SET gcode_file_path = ? WHERE id = ?", (path, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()



db = Database('store.db')

# db.insert("/gcodes/square.nc")