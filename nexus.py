import os
from tkinter import filedialog
from tkinter import *
from db import Database
from widgets.Laser import LaserConfig

db = Database('store.db')
app = Tk()
# fetch gets one record. [1] is the 2 list item containing the path
defaultGcode = db.defaultGcodePathFetch()[1]
state = {
    "laser1": {
        "status" : "0",
        "config" : {}
    },
    "laser2": {
        "status" : "0",
        "config" : {}
    },
    "laser3": {
        "status" : "0",
        "config" : {}
    },
    "laser4": {
        "status" : "0",
        "config" : {}
    }
}

app.title('Nexus')
app.geometry('720x350')

for laserNum in range(4):
    state["laser"+str(laserNum+1)]["config"] = LaserConfig(app, laserNum+1)
    
    
print(state['laser3']['config'].laserNum)

app.mainloop()
