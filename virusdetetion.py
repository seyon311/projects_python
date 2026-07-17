from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("175x200")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

button = Button(window, text="Scan for virus", command=msg) # command=msg is the action
button.place(x=40, y=80)

window.mainloop()
