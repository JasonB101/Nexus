import os
from tkinter import *
from db import Database
from widgets.Laser import LaserConfig
from widgets.BurnControl import BurnControl
from functions.getComPorts import getComPorts
from functions.runJobs import runJobs

db = Database('store.db')
app = Tk()
# fetch gets one record. [1] is the 2 list item containing the path
defaultProfileName = os.path.basename(db.getSettings()[1])
numberOfLasers = 3

lasers = []
for i in range(numberOfLasers):
    lasers.append(LaserConfig(app, i+1, getComPorts(), defaultProfileName))


app.title('Nexus')
app.geometry('720x350')
    
burnControl = BurnControl(app, lasers, runJobs)

if __name__ == '__main__':
    app.mainloop()
