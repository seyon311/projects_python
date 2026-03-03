n = int(input("Enter a positive integer: "))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f"The sum of the first {n} natural numbers is: {sum}")