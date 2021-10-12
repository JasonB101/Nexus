import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS settings (id INTEGER PRIMARY KEY, defaultProfile text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS profiles (profilename text PRIMARY KEY, filepath text, power int, speed int)")
        self.conn.commit()

        #Need to create a model for the burning profile. (Filename linked to speed and power)

    
    def fetchProfile(self, profilename):
        self.cur.execute("SELECT * FROM profiles WHERE profilename= ?", (profilename,))
        profile = self.cur.fetchone()
        return profile
    
    def saveProfile(self, profile):
        profilename = profile.get('profilename', None)
        filepath = profile.get('filepath', None)
        power = profile.get('power', None)
        speed = profile.get('speed', None)
        self.cur.execute("INSERT or REPLACE INTO profiles(profilename, filepath, power, speed) VALUES(?,?,?,?)", (profilename, filepath, power, speed))
        self.conn.commit()
        print("saved",profilename,filepath,power,speed)
    
    def getSettings(self):
        self.cur.execute("SELECT * FROM settings")
        defaultPath = self.cur.fetchone()
        return defaultPath
        
    def insertSettings(self, defaultProfile):
        self.cur.execute("INSERT or REPLACE INTO settings(id, defaultProfile) VALUES (77, ?)", (defaultProfile,))
        self.conn.commit()

    def removeSettings(self, id):
        self.cur.execute("DELETE FROM settings WHERE id=?", (id,))
        self.conn.commit()

    def updateSettings(self, id, path):
        self.cur.execute("UPDATE settings SET defaultProfile = ? WHERE id = ?", (path, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()



db = Database('store.db')

# db.insert("/gcodes/square.nc")