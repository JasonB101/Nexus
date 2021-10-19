import os
from tkinter import *
from db import Database
from widgets.Laser import LaserConfig
from widgets.BurnControl import BurnControl
from functions.getComPorts import getComPorts
from classes.Job import Job
from functions.getResponse import getResponse
import multiprocessing as mp


db = Database('store.db')
app = Tk()
# fetch gets one record. [1] is the 2 list item containing the path
defaultProfileName = os.path.basename(db.getSettings()[1])
comPorts = getComPorts()
numberOfLasers = 2

lasers = []

app.title('Nexus')
app.geometry('720x350')


for i in range(numberOfLasers):
    lasers.append(LaserConfig(app, i+1, comPorts, defaultProfileName))
    
def runJob(job):
    getResponse(job.port)

def runJobs():
    jobs = []
    for laser in lasers:
        jobs.append(Job(laser))
        
    for job in jobs:
        mp.freeze_support()
        proc = mp.Process(target=runJob, args=(job,))
        proc.start()
    
burnControl = BurnControl(app, lasers, runJobs)

app.mainloop()
