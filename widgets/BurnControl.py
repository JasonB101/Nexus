import os
import tkinter as tk
from tkinter import CENTER
from db import Database
from classes.Job import Job
db = Database('store.db')

class BurnControl:
    def __init__(self, app, lasers, runJobs):
        def printDetails():
            for laser in lasers:
                print(laser.profilename, laser.port(), laser.speed(), laser.power())
                
        def saveProfiles():
            for laser in lasers:
                profile = buildProfile(laser)
                db.saveProfile(profile)
        
        def buildProfile(laserConfig):
            profile = {
                "profilename": laserConfig.profilename,
                "filepath": laserConfig.filepath,
                "power": laserConfig.power(),
                "speed": laserConfig.speed(),
            }
            return profile
        
        def startJobs():         
            runJobs()
                
            # for job in jobs:
            #     job.getResponse()
                
            # printDetails()
            # saveProfiles()
            
        self.button = tk.Button(app, text="Start", command = startJobs)
        self.button.grid(row=2, column=0)
        self.button.place(relx=0.01, rely=0.6)