from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Interest Calculator")
window.geometry("600x600")

def calculate_simple_interest():
    simple_interest = Principal*Rate*Time
    return simple_interest

def calculate_compound_interest():
   compound_interest = Principal*((1+(Rate/Amtoftimes))**(Amtoftimes*Time))
   return compound_interest

def run_simple():
    global Principal, Rate, Time
    try:
        Principal = float(principal_entry.get())
        Rate = float(rate_entry.get()) / 100
        Time = float(time_entry.get())

        si = calculate_simple_interest()
        result_label.config(text=f"Simple Interest: £{si:.5f}")
    except:
        messagebox.showerror("Error", "Enter valid numbers")

def run_compound():
    global Principal, Rate, Time, Amtoftimes
    try:
        Principal = float(principal_entry.get())
        Rate = float(rate_entry.get()) / 100
        Time = float(time_entry.get())
        Amtoftimes = float(times_entry.get())

        ci = calculate_compound_interest()
        result_label.config(text=f"Compound Amount: £{ci:.5f}")
    except:
        messagebox.showerror("Error", "Enter valid numbers")


Label(window, text="Principal:", font=("Arial", 16)).pack()
principal_entry = Entry(window, font=("Arial", 16))
principal_entry.pack(pady=10)

Label(window, text="Rate (%):", font=("Arial", 16)).pack()
rate_entry = Entry(window, font=("Arial", 16))
rate_entry.pack(pady=10)

Label(window, text="Time (years):", font=("Arial", 16)).pack()
time_entry = Entry(window, font=("Arial", 16))
time_entry.pack(pady=10)

Label(window, text="Times Compounded Per Year:", font=("Arial", 16)).pack()
times_entry = Entry(window, font=("Arial", 16))
times_entry.pack(pady=10)

Button(window, text="Calculate Simple Interest", font=("Arial", 16),
       command=run_simple).pack(pady=20)

Button(window, text="Calculate Compound Interest", font=("Arial", 16),
       command=run_compound).pack(pady=20)

result_label = Label(window, text="", font=("Arial", 20), fg="blue")
result_label.pack(pady=30)

window.mainloop()
