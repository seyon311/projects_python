print("Right Angled Pattern of Asterisks (*)")
n = int(input("Enter the number of rows: "))

for i in range(1, n+1, 1):
    for j in range(1, i+1, 1):
        print("* ", end="")
    print() # Move to the next line after each row is printed    