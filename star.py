import turtle as t
t.Screen().bgcolor("black")
t.color("aqua")
t.penup()
t.Screen().setup(500, 500)
t.goto(-40, -40)
t.pendown()

side_length = 60

t.left(60)
t.forward(side_length)
t.right(120)
t.forward(side_length)
t.right(120)
t.forward(side_length)
t.penup()

t.goto(-40, 40)

t.pendown()


t.left(120)
t.forward(side_length)
t.left(120)
t.forward(side_length)
t.left(120)
t.forward(side_length)




t.done()