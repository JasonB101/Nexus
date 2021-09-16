import os
from tkinter import filedialog
from tkinter import *
from db import Database

db = Database('store.db')
app = Tk()
# fetch gets one record. [1] is the 2 list item containing the path
defaultGcode = db.fetch()[1]
store = {
    "laser1": {
        "path": defaultGcode,
        "status" : "0"
    },
    "laser2": {
        "path": defaultGcode,
        "status" : "0"
    },
    "laser3": {
        "path": defaultGcode,
        "status" : "0"
    },
    "laser4": {
        "path": defaultGcode,
        "status" : "0"
    }
}

def changeGcodePath(newPath):
    db.update(77, newPath)

def handleButton(num, labelPath):
    filePath = filedialog.askopenfilename()
    if (num == 1):
        changeGcodePath(filePath)
    laser = "laser"+ str(num)
    store[laser]["path"] = filePath
    labelPath.configure(text=os.path.basename(store[laser]["path"]))
    print(store)


app.title('Nexus')
app.geometry('720x350')

frame1 = Frame(app, width=150, height = 150, highlightthickness=1, highlightbackground='black')
frame1.grid(row=0, column=0, pady = 10, padx = 10, ipady = 5, ipadx = 5)
frame1.grid_propagate(False)
labelPath1 = Label(frame1, text=os.path.basename(store["laser1"]["path"]))
labelPath1.grid(row=0, column=0)
labelPath1.place(relx=0.5, rely=0.1, anchor=CENTER)
button1 = Button(frame1, text="Load", command = lambda: handleButton(1, labelPath1))
button1.grid(row=10, column=0)
button1.place(relx=0.5, rely=0.9, anchor=CENTER)

frame2 = Frame(app, width=150, height = 150, highlightthickness=1, highlightbackground='black')
frame2.grid(row=0, column=1, pady = 10, padx = 10, ipady = 5, ipadx = 5)
frame2.grid_propagate(False)
labelPath2 = Label(frame2, text=os.path.basename(store["laser2"]["path"]))
labelPath2.grid(row=0, column=0)
labelPath2.place(relx=0.5, rely=0.1, anchor=CENTER)
button2 = Button(frame2, text="Load", command = lambda: handleButton(2, labelPath2))
button2.grid(row=10, column=0)
button2.place(relx=0.5, rely=0.9, anchor=CENTER)

frame3 = Frame(app, width=150, height = 150, highlightthickness=1, highlightbackground='black')
frame3.grid(row=0, column=2, pady = 10, padx = 10, ipady = 5, ipadx = 5)
frame3.grid_propagate(False)
labelPath3 = Label(frame3, text=os.path.basename(store["laser3"]["path"]))
labelPath3.grid(row=0, column=0)
labelPath3.place(relx=0.5, rely=0.1, anchor=CENTER)
button3 = Button(frame3, text="Load", command = lambda: handleButton(3, labelPath3))
button3.grid(row=10, column=0)
button3.place(relx=0.5, rely=0.9, anchor=CENTER)

frame4 = Frame(app, width=150, height = 150, highlightthickness=1, highlightbackground='black')
frame4.grid(row=0, column=3, pady = 10, padx = 10, ipady = 5, ipadx = 5)
frame4.grid_propagate(False)
labelPath4 = Label(frame4, text=os.path.basename(store["laser4"]["path"]))
labelPath4.grid(row=0, column=0)
labelPath4.place(relx=0.5, rely=0.1, anchor=CENTER)
button4 = Button(frame4, text="Load", command = lambda: handleButton(4, labelPath4))
button4.grid(row=10, column=0)
button4.place(relx=0.5, rely=0.9, anchor=CENTER)

app.mainloop()
