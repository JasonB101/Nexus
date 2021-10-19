import os
import tkinter as tk
from tkinter import CENTER
from tkinter import filedialog
from tkinter import ttk
from db import Database

db = Database('store.db')
    
class LaserConfig:
    def __init__(self, app, laserNum, ports, defaultProfileName):
        def openNewPath():
            self.filepath = filedialog.askopenfilename()
            filename = os.path.basename(self.filepath)
            self.profilename = filename
            profile = db.fetchProfile(filename)
            loadProfile(profile)
            self.labelPath.configure(text=filename)
        
            if (laserNum == 1):
                db.insertSettings(filename) #change default GCode path, 77 is a random ID I chose 
        
        self.filepath = ""
        self.powerVar = tk.StringVar()
        self.speedVar = tk.StringVar()
        self.portVar = tk.StringVar()
        self.portVar.set(ports[laserNum-1])
        self.power = lambda: self.powerVar.get()
        self.speed = lambda: self.speedVar.get()
        self.port = lambda: self.portVar.get()
        self.profilename = defaultProfileName
        self.laserNum = laserNum
        #View
        self.frame = tk.Frame(app, width=150, height = 150, highlightthickness=1, highlightbackground='black')
        self.labelPath = tk.Label(self.frame, text=self.profilename)
        self.button = tk.Button(self.frame, text="Open", command = openNewPath)
        self.labelPower = tk.Label(self.frame, text="power:")
        self.labelSpeed = tk.Label(self.frame, text="speed:")
        self.labelPort = tk.Label(self.frame, text="usb port:")
        self.entryPower = tk.Entry(self.frame, textvariable=self.powerVar, width=5, )
        self.entrySpeed = tk.Entry(self.frame, textvariable=self.speedVar, width=5)
        #ComboBox Details
        self.comboBoxPort = ttk.Combobox(self.frame, textvariable=self.portVar, width=8, state="readonly", values=ports)
        self.comboBoxPort.bind('<<ComboboxSelected>>', lambda e: self.portVar.set(e.widget.get()))
        
        #Details
        self.frame.grid_propagate(False)
        self.frame.grid(row=0, column=laserNum, pady = 10, padx = 10, ipady = 5, ipadx = 5)
        ####
        self.labelPath.grid(row=0, column=1)
        self.labelPower.grid(row=3, column=0)
        self.entryPower.grid(row=3, column=2)
        self.labelSpeed.grid(row=6, column=0)
        self.entrySpeed.grid(row=6, column=2)
        self.comboBoxPort.grid(row=9, column=2)
        self.labelPort.grid(row=9, column=0)
        self.button.grid(row=10, column=1)
        ####
        self.labelPath.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.labelPower.place(relx=0.3, rely=0.3, anchor=CENTER)
        self.labelSpeed.place(relx=0.3, rely=0.5, anchor=CENTER)
        self.labelPort.place(relx=0.3, rely=0.7, anchor=CENTER)
        self.entryPower.place(relx=0.7, rely=0.3, anchor=CENTER)
        self.entrySpeed.place(relx=0.7, rely=0.5, anchor=CENTER)
        self.comboBoxPort.place(relx=0.7, rely=0.7, anchor=CENTER)
        self.button.place(relx=0.5, rely=0.9, anchor=CENTER)
       
        def initialSetup():
            profile = db.fetchProfile(defaultProfileName)
            loadProfile(profile)
            
            
        def loadProfile(profile):
            #(profilename, filepath, power, speed)
            #profile is returned as a tuple
            if (profile):
                self.powerVar.set(profile[2])
                self.speedVar.set(profile[3])
                self.filepath = profile[1]
            else:
                self.powerVar.set(75)
                self.speedVar.set(20)
            
        initialSetup()