import os
import tkinter as tk
from tkinter import CENTER
from db import Database
db = Database('store.db')

class BurnControl:
    def __init__(self, app, lasers, startJobs, messageBox):
        def printDetails():
            for laser in lasers:
                messageBox.insertMessage(f'{laser.profilename} {laser.port()} {laser.speed()} {laser.power()}')
                
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
        
        def start():
            messageBox.insertMessage(f'Starting Jobs on {len(lasers)} lasers')        
            startJobs(lasers, messageBox)
            # saveProfiles()
            
        self.button = tk.Button(app, text="Start", command = start)
        self.button.grid(row=3, column=0)
        self.button.place(relx=0.01, rely=0.915)