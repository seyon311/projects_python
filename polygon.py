import turtle as t
t.Screen().bgcolor("black")
t.color("aqua")
t.penup()
t.Screen().setup(500, 500)
t.goto(0, 0)
t.pendown()

num_sides = int(input("Enter the number of sides for the polygon: "))
angle = 360 / num_sides
sidelength = 100

for i in range(0, num_sides, 1):
    t.forward(sidelength)
    t.right(angle)

t.done()    
