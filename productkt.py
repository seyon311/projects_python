import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("975x400")

def calculate_product():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        product = num1 * num2
        label_result.config(text=f"Product: {product}")
    except ValueError:
        label_result.config(text="Please enter valid numbers.")

def calculate_sum():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        sum = num1 + num2
        label_result.config(text=f"Sum: {sum}")
    except ValueError:
        label_result.config(text="Please enter valid numbers.")

def calculate_difference():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        difference = num1 - num2
        label_result.config(text=f"Difference: {difference}")
    except ValueError:
        label_result.config(text="Please enter valid numbers.")

def calculate_quotient():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            label_result.config(text="Cannot divide by zero.")
        else:
            quotient = num1 / num2
            label_result.config(text=f"Quotient: {quotient}")
    except ValueError:
        label_result.config(text="Please enter valid numbers.")        

def calculate_exponential():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 ** num2
        label_result.config(text=f"Exponential: {result}")
    except ValueError:
        label_result.config(text="Please enter valid numbers.")



label_num1 = tk.Label(window, text="Enter first number:")
label_num2 = tk.Label(window, text="Enter second number:")
entry_num1 = tk.Entry(window)
entry_num2 = tk.Entry(window)

button_calculate = tk.Button(window, text="Calculate Product", command=calculate_product)
button_sum = tk.Button(window, text="Calculate Sum", command=calculate_sum)
button_difference = tk.Button(window, text="Calculate Difference", command=calculate_difference)
button_quotient = tk.Button(window, text="Calculate Quotient", command=calculate_quotient)
button_exponential = tk.Button(window, text="Calculate Exponential", command=calculate_exponential)

label_result = tk.Label(window, text="Answer : ")

label_description = tk.Label(window, text="This is a simple calculator that can perform multiplication, addition, subtraction, division, and exponentiation on two numbers. Type in 0.5 for sqrt and 0.333 for cube root.")

label_newline = tk.Label(window, text="\n")
label_newline2 = tk.Label(window, text="\n")
label_newline3 = tk.Label(window, text="\n")
label_newline4 = tk.Label(window, text="\n")

label_num1.pack()
entry_num1.pack()
label_num2.pack()
entry_num2.pack()

label_newline.pack()

button_calculate.pack()
button_sum.pack()
button_difference.pack()
button_quotient.pack()
button_exponential.pack()

label_newline2.pack()

label_result.pack()
label_newline3.pack()
label_description.pack()
label_newline4.pack()

window.mainloop()