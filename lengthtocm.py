from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Converter")
root.geometry("500x150")

def convert():
    try:
        inches = float(entry_inches.get())
        cm = inches * 2.54
        messagebox.showinfo("Result", f"{inches} inches is {cm} cm")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

label_inches = Label(root, text="Inches :")
label_inches.pack()

entry_inches = Entry(root)
entry_inches.pack()

button_cal = Button(root, text="Calculate", command=convert)
button_cal.pack()

root.mainloop()
