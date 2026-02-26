n = int(input("Enter a positive integer to calculate the sum of whole numbers up to that whole number: "))

if n < 0:
    print("Invalid input. Please enter a positive integer.")
else:

    sum = 0
    for i in range(1, n + 1, 1):
        sum += i

    print(f"The sum of whole numbers up to {n} is: {sum}")    