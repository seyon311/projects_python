num = str(input("Enter a 3+-digit number: "))

if not num.isdigit() or len(num) < 3:
    print("Invalid input. Please enter a valid 3+-digit number.")

else:
    mid = len(num) // 2
    MidOne, MidTwo = num[mid - 1], num[mid]

    product = int(MidOne) * int(MidTwo)
    
    print(f"The middle digits are: {MidOne} and {MidTwo}")
    print(f"The product of the middle digits is: {product}")
    



