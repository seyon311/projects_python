def factorial(n):
    for i in range(1, n):
        n *= i
    return n

number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}")
    