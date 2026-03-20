import math as m

def circumference(radius):
    return 2 * m.pi * radius

radius = float(input("Enter the radius of the circle: "))
print(f"The circumference of the circle with radius {radius} is: {circumference(radius)}")