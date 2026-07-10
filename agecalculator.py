from tkinter import *
from tkinter import messagebox
from datetime import datetime

window = Tk()
window.title("Age Calculator")
window.geometry("400x300")

def Solve_age(year, month, day):
    if not year or not month or not day:
        messagebox.showerror("Error", "All fields must be filled.")
        return
    
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        messagebox.showerror("Error", "Please enter valid numeric values.")
        return
    
    year = int(year)
    month = int(month)
    day = int(day)

    # Month validation
    if month < 1 or month > 12:
        messagebox.showerror("Error", "Please enter a valid month (1-12).")
        return
    
    # Day validation by month
    if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
        messagebox.showerror("Error", "Please enter a valid day (1-31).")
        return
    
    if month in [4, 6, 9, 11] and (day < 1 or day > 30):
        messagebox.showerror("Error", "Please enter a valid day (1-30).")
        return
    
    # February validation
    if month == 2:
        leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if leap and (day < 1 or day > 29):
            messagebox.showerror("Error", "Valid day for February in a leap year is 1-29.")
            return
        if not leap and (day < 1 or day > 28):
            messagebox.showerror("Error", "Valid day for February in a non-leap year is 1-28.")
            return
    
    # Year validation
    current_year = datetime.now().year
    if year < 1900 or year > current_year:
        messagebox.showerror("Error", "Please enter a valid year (1900 to current year).")
        return
    
    # Future date check
    today = datetime.now()
    try:
        birth_date = datetime(year, month, day)
    except:
        messagebox.showerror("Error", "Invalid date.")
        return

    if birth_date > today:
        messagebox.showerror("Error", "Birth date cannot be in the future.")
        return

    # --- AGE CALCULATION ---
    age_years = today.year - birth_date.year
    age_months = today.month - birth_date.month
    age_days = today.day - birth_date.day

    if age_days < 0:
        age_months -= 1
        age_days += 30  # approximate

    if age_months < 0:
        age_years -= 1
        age_months += 12

    messagebox.showinfo("Your Age",
                        f"You are {age_years} years, {age_months} months, and {age_days} days old.")

label_title = Label(window, text="Age Calculator", font=("Arial", 16))
label_title.pack(pady=10)

label_year = Label(window, text="Enter your birth year : ")
label_year.pack()
entry_year = Entry(window)
entry_year.pack()

label_month = Label(window, text="Enter your birth month : ")
label_month.pack()
entry_month = Entry(window)
entry_month.pack()

label_day = Label(window, text="Enter your birth day : ")
label_day.pack()
entry_day = Entry(window)
entry_day.pack()

button_calculate = Button(window, text="Calculate Age",
                          command=lambda: Solve_age(entry_year.get(), entry_month.get(), entry_day.get()))
button_calculate.pack(pady=10)

window.mainloop()
