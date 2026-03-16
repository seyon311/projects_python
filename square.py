import turtle as t
t.Screen().bgcolor("black")
t.color("aqua")
t.penup()
t.Screen().setup(500, 500)
t.goto(0, 0)
t.pendown()
t.speed(100)

input("Press Enter to draw a square")
for i in range(4):
    t.forward(100)
    t.right(90)

t.done()