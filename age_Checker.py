age = int(input("Enter your age: "))

if age <= 0:
    print("Invalid input. Age cannot be negative.")
elif age > 1 and age < 10:
    print(f"You are too young to enter Raj's class. You may enter after {10 - age} years.")    
elif age >= 10 and age < 21:
    print(f"You are eligible to enter Raj's class. You may enter now.")
else:
    print(f"You are too old to enter Raj's class. You could have entered {(age - 20) + 10} years before.")    