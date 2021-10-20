import tkinter as tk
from datetime import *
class Messages:
    def __init__(self, app):
        self.listBox = tk.Listbox(app, width=116)
        self.listBox.grid(row=2, column=0)
        self.listBox.place(relx=0.01, rely=0.45)
        
        def insert(string):
            timeNow = datetime.now().strftime("%H:%M:%S")
            withTime = str(f'[{timeNow}]: {string}')
            self.listBox.insert(tk.END, withTime)
            
        self.insertMessage = lambda string: insert(string)
