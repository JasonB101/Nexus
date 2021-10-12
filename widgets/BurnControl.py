import os
import tkinter as tk
from tkinter import CENTER
from db import Database
db = Database('store.db')

class BurnControl:
    def __init__(self, app, lasers):
        def printDetails():
            for laser in lasers:
                config = laser.get('config', None)
                print(config.profilename, config.port(), config.speed(), config.power())
                
        def saveProfiles():
            for laser in lasers:
                profile = buildProfile(laser)
                db.saveProfile(profile)
        
        def buildProfile(object):
            config = object.get('config', None)
            profile = {
                "profilename": config.profilename,
                "filepath": config.filepath,
                "power": config.power(),
                "speed": config.speed(),
            }
            return profile
        
        def startJobs():
            printDetails()
            saveProfiles()
            
        self.button = tk.Button(app, text="Start", command = startJobs)
        self.button.grid(row=2, column=0)
        self.button.place(relx=0.01, rely=0.6)