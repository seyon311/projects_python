import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius ** 2
        print(f"The area of a circle with a radius of {self.radius} is {area} ")
    def circumference(self):
        circumference = 2 * math.pi * self.radius
        print(f"The circumference of a circle with a radius of {self.radius} is {circumference}")

R = int(input("Enter radius : "))

circle = Circle(R)

circle.area()
circle.circumference()
