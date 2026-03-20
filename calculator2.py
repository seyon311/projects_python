def calculator(operation):
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        if y == 0:
            return "Error: Division by zero is not allowed."
        return x / y
    def power(x, y):
        return x ** y
    
    if operation == "add":
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        print(f"The result of {x} + {y} is: {add(x, y)}")
    elif operation == "subtract":
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        print(f"The result of {x} - {y} is: {subtract(x, y)}")
    elif operation == "multiply":
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        print(f"The result of {x} * {y} is: {multiply(x, y)}")
    elif operation == "divide":
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        print(f"The result of {x} / {y} is: {divide(x, y)}")
    elif operation == "power":
        x = float(input("Enter the base: "))
        y = float(input("Enter the exponent: "))
        print(f"The result of {x} ^ {y} is: {power(x, y)}")
    else:
        print("Invalid operation. Please choose from add, subtract, multiply, divide, or power.")    

input_operation = input("Enter the operation (add, subtract, multiply, divide, power): ")
calculator(input_operation)



