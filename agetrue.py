try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid age.")
else:
    if age < 1:
        print("Age cannot be less than 1.")
    elif age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")
finally:
    print("Program complete.")