import os
import tkinter as tk
from tkinter import CENTER
from tkinter import filedialog
from db import Database

db = Database('store.db')


    
    
class LaserConfig:
    def __init__(self, app, laserNum):
        def openNewPath():
            self.filePath = filedialog.askopenfilename()
            filename = os.path.basename(self.filePath)
            profile = db.fetchProfile(filename)
            
            if (profile.filename):
                self.powerVar.set(profile.power)
                self.speedVar.set(profile.speed)
                
            self.labelPath.configure(filename)
        
            if (self.laserNum == 1):
                db.update(77, self.filePath) #change default GCode path, 77 is a random ID I chose            
    
        self.laserNum = laserNum
        self.filePath = db.defaultGcodePathFetch()[1]
        self.filename = os.path.basename(self.filePath)
        self.port = "usb/tty"
        self.powerVar = tk.StringVar()
        self.speedVar = tk.StringVar()
        self.power = lambda: self.powerVar.get()
        self.speed = lambda: self.speedVar.get()
        #View
        self.frame = tk.Frame(app, width=150, height = 150, highlightthickness=1, highlightbackground='black')
        self.labelPath = tk.Label(self.frame, text=self.filename)
        self.button = tk.Button(self.frame, text="Open", command = openNewPath)
        self.labelPower = tk.Label(self.frame, text="power:")
        self.labelSpeed = tk.Label(self.frame, text="speed:")
        self.entryPower = tk.Entry(self.frame, textvariable=self.powerVar, width=5, )
        self.entrySpeed = tk.Entry(self.frame, textvariable=self.speedVar, width=5)
        #Details
        self.frame.grid_propagate(False)
        self.frame.grid(row=0, column=laserNum, pady = 10, padx = 10, ipady = 5, ipadx = 5)
        ####
        self.labelPath.grid(row=0, column=1)
        self.labelPower.grid(row=3, column=0)
        self.entryPower.grid(row=3, column=2)
        self.labelSpeed.grid(row=6, column=0)
        self.entrySpeed.grid(row=6, column=2)
        self.button.grid(row=10, column=1)
        ####
        self.labelPath.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.labelPower.place(relx=0.3, rely=0.3, anchor=CENTER)
        self.labelSpeed.place(relx=0.3, rely=0.6, anchor=CENTER)
        self.entryPower.place(relx=0.7, rely=0.3, anchor=CENTER)
        self.entrySpeed.place(relx=0.7, rely=0.6, anchor=CENTER)
        self.button.place(relx=0.5, rely=0.9, anchor=CENTER)
        
        
        
        