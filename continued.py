var = int(input("Enter a positive integer: "))
missing = int(input("Enter a number to skip: "))

if missing > var or missing < 0:
    print("The number to skip must be less than or equal to the positive integer.")

while var > 0:
    var -= 1
    if var == missing:
        continue
    else:
        print(f"Current value: {var}")
