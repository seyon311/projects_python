from tkinter import *


window = Tk()
window.geometry("300x200")
window.title("Start Program")

def open_scheduler():
    # Create the new window
    top = Toplevel(window)
    top.geometry("400x300")
    top.title("Reading Scheduler")

    # Labels
    label1 = Label(top, text="How many pages are in the book?")
    label2 = Label(top, text="How many pages do you read per day?")
    label3 = Label(top, text="How many pages have you already read?")

    label1.pack()
    label2.pack()
    label3.pack()

    # Entry fields
    entry_total = Entry(top)
    entry_per_day = Entry(top)
    entry_read = Entry(top)

    entry_total.pack()
    entry_per_day.pack()
    entry_read.pack()

    # Result label
    result_label = Label(top, text="")
    result_label.pack()

    def calculate():
        total_pages = int(entry_total.get())
        pages_per_day = int(entry_per_day.get())
        pages_read = int(entry_read.get())

        remaining_pages = total_pages - pages_read
        days_needed = remaining_pages / pages_per_day

        result_label.config(
            text=f"You will finish the book in {days_needed:.1f} days.\n"
                 f"You have {remaining_pages} pages left to read."
        )

    btnsolve = Button(top, text="Calculate", command=calculate)
    btnsolve.pack()

# Main window button
start_btn = Button(window, text="Would you like to start the program?", command=open_scheduler)

start_btn.pack(expand=True)

window.mainloop()
