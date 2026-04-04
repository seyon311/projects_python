import math

x = float(input("Enter an angle in degrees: ").strip())

print(f"The sine of {x} degrees is {math.sin(math.radians(x))}.")
print(f"The cosine of {x} degrees is {math.cos(math.radians(x))}.")
print(f"The tangent of {x} degrees is {math.tan(math.radians(x))}.")