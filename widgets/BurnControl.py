import os
import tkinter as tk
from tkinter import CENTER
from db import Database

class BurnControl:
    def __init__(self, app, lasers):
        def getDetails():
            for laser in lasers:
                config = laser.get('config', None)
                print(config.filename, config.port(), config.speed(), config.power())
                
        self.button = tk.Button(app, text="Get Details", command = getDetails)
        self.button.grid(row=2, column=0)
        self.button.place(relx=0.01, rely=0.6)