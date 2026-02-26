n = int(input("Enter a positive integer which you want to reverse: "))  

if n < 0:   
    print("Invalid input. Please enter a positive integer.")
else:
    print(f"\nthe {n} to 1 are :")
    for i in range(n, 0, -1):
        print(i)