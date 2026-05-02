# There is a few bugs in this code that I don't know how to fix, line 17 and line 21 are the ones I can't fix

print("Welcome to the list generator and function applicator!")

again = True

while again: # Main loop to allow multiple runs
    x = int(input("Enter a number between 10 and 50: ")) # Initial input

    while x < 10 or x > 50:  # Correction loop
        print("Invalid input.")
        x = int(input("Please re-enter a number between 10 and 50: "))

    numbers = [i for i in range(1, x + 1)]
    print("Generated list:", numbers)

    multiplier = float(input("Type in a number to multiply each element in the list, NOTE : PLEASE don't write 1/x to divide"))

    if multiplier != float and multiplier != int:
        print("Invalid input. Please enter a valid number.")
        multiplier = float(input("Type in a number to multiply each element in the list, NOTE : PLEASE don't write 1/x to divide"))

    result = [i * multiplier for i in numbers]

    print("Result after multiplication/division:", result)

    adder = float(input("Type in a number to add to each element in the list NOTE : write -x to subtract where x is the number to be subtracted: "))

    result = [i + adder for i in result]

    print("Final result:", result)

    if multiplier == 1:
        multiplier = ""
    if adder == 0:
        adder = "" 
        print(f"The function you have applied to the FIRST list to the LAST list is : {multiplier}x {adder}")
    else:
        print(f"The function you have applied to the FIRST list to the LAST list is : {multiplier}x + {adder}")

    again = input("Do you want to generate another list? (y/n): ")

    if again.lower() != 'y':
        again = False

print("Thank you for using the list generator and function applicator! Goodbye!")

