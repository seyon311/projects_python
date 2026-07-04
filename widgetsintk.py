from tkinter import *
from datetime import date

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

root = Tk()
root.title("Getting started with Widgets")
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

lbl = Label(text = "Hello There!", fg = "#ffffff", bg = "#000000", height = 1, width = 300)

name_lbl = Label(text = "Full name", bg = "#3895D3")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message

    message = "Welcome to the application! \nToday's date is : "
    greet = "\n\nHello " + name + "!\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height = 3)

btn = Button(text = "Begin", command = display, height = 1, bg = "#1261A0", fg = "#ffffff")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()