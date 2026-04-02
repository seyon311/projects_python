invalid = False
while not invalid:
    try:
        n = int(input("Enter a positive integer: "))

        while n % 2 == 0:
            print("Infinite, bye bye!")
        invalid = True
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
    finally:
        print("Program complete.") 
               