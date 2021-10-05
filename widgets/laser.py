import os
import tkinter as tk
from tkinter import filedialog
from tkinter import tkk
from .. import Database

db = Database('store.db')

def openNewPath(self):
            self.filePath = filedialog.askopenfilename()
            self.labelPath.configure(text=os.path.basename(self.filePath))
        
            if (self.laserNum == 1):
                db.update(77, self.filePath) #change default GCode path
                
class LaserConfig:
    def __init__(self, app, laserNum):
        self.laserNum = laserNum
        self.filePath = db.defaultGcodePathFetch()[1]
        self.power = 0
        self.speed = 0
        self.port = "usb/tty"
        #View
        self.frame = tk.Frame(app, width=150, height = 150, highlightthickness=1, highlightbackground='black')
        self.labelPath = tk.Label(self.frame, text=os.path.basename(self.filePath))
        tk.Button(self.frame, text="Open", command = openNewPath)
        #Details
        self.frame.grid(row=0, column=laserNum, pady = 10, padx = 10, ipady = 5, ipadx = 5)
        self.frame.grid_propagate(False)
                
    # frame = tk.Frame(app, width=150, height = 150, highlightthickness=1, highlightbackground='black')
    # frame.grid(row=0, column=laserNum, pady = 10, padx = 10, ipady = 5, ipadx = 5)
    # frame.grid_propagate(False)
    # labelPath = tk.Label(frame, text=filename)
    # labelPath.grid(row=0, column=0)
    # labelPath.place(relx=0.5, rely=0.1, anchor=CENTER)
    # button = tk.Button(frame2, text="Open", command = openNewPath)
    # button.grid(row=10, column=0)
    # button.place(relx=0.5, rely=0.9, anchor=CENTER)