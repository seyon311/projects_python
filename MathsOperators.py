import math

number = float(input("Enter a irregular decimal number: ").strip())

print(f"The ceiling of {number} is {math.ceil(number)} and the floor is {math.floor(number)}.")

p = int(input("Enter a positive integer = x: ").strip())
n = int(input("Enter a negative integer = y: ").strip())

print(f"The value of x after copying the sign from y is {math.copysign(p, n)}.")
print(f"And the absolute value of y is {math.fabs(n)}.")

p2 = int(input("Enter another positive integer = z:").strip())

print(f"The Highest Common Factor of {p} and {p2} is {math.gcd(p, p2)}.")