try:
    n1, n2 = eval(input("Enter two numbers separated by comma: "))
    quotient = n1 / n2
    print("The quotient is:", quotient)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except SyntaxError:
    print("Invalid input format. Please enter two numbers separated by a comma.")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
else:
    print("Division performed successfully, no exceptions occurred.")
finally:
    print("Execution of the program is complete - this will always be executed.\n")                    
                  