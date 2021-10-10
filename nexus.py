import os
from tkinter import filedialog
from tkinter import *
from db import Database
from widgets.Laser import LaserConfig
from widgets.BurnControl import BurnControl
from functions.getComPorts import getComPorts

db = Database('store.db')
app = Tk()
# fetch gets one record. [1] is the 2 list item containing the path
defaultProfileName = os.path.basename(db.getSettings()[1])
comPorts = getComPorts()
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

for i in range(4):
    state["laser"+str(i+1)]["config"] = LaserConfig(app, i+1, comPorts, defaultProfileName)
    
lasers = []
for i in state:
    lasers.append(state[i])
    
burnControl = BurnControl(app, lasers)
    

app.mainloop()
