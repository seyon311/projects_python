from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("My Window")
window.geometry("700x300")

def submit_form(name, gmail, password, confirm_password):
    if not name or not gmail or not password or not confirm_password:
        messagebox.showerror("Error", "All fields must be filled.")
        return
    
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return
    
    if gmail.endswith("@gmail.com") and len(gmail) > 10:
        messagebox.showinfo("Success", "Account created successfully!")
    else:
        messagebox.showerror("Error", "Please enter a valid Gmail address.")

label_Account = Label(window, text="Create your account", font=("Arial", 16))

label_name = Label(window, text="Please enter your username (Don't make it your real name):")
label_gmail = Label(window, text="Please enter your GMAIL:")
label_password = Label(window, text="Please enter your password:")
label_confirm_password = Label(window, text="Please confirm your password:")

entry_name = Entry(window)
entry_gmail = Entry(window)
entry_password = Entry(window, show="*")
entry_confirm_password = Entry(window, show="*")

button_submit = Button(
    window,
    text="Submit",
    command=lambda: submit_form(
        entry_name.get(),
        entry_gmail.get(),
        entry_password.get(),
        entry_confirm_password.get()
    )
)

label_Account.pack(pady=10)

label_name.pack()
entry_name.pack()

label_gmail.pack()
entry_gmail.pack()

label_password.pack()
entry_password.pack()

label_confirm_password.pack()
entry_confirm_password.pack()

button_submit.pack(pady=10)

window.mainloop()
