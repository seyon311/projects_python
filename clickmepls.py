from tkinter import *

window = Tk()

window.title("Click Me!")
window.geometry("100x50")

def handle_click(event):
    print(event.char, "Key was pressed") # Print the character associated to the key pressed

window.bind("<Key>", handle_click)

def handle_click(event):
    print("\nThe button was clicked!")

button = Button(text="Click me!")
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()