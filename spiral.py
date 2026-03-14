import turtle as t
import random as r
t.colormode(255)

R = r.randint(0, 255)
G = r.randint(0, 255)
B = r.randint(0, 255)

t.Screen().bgcolor("black")
t.color("aqua")
t.penup()
t.Screen().setup(1920, 1080)
t.goto(-40, -40)
t.pendown()
t.speed(100)

size = 0


while counter < 10:

    R = r.randint(0, 255)
    G = r.randint(0, 255)
    B = r.randint(0, 255)

    t.color((R, G, B))

    for i in range(0, 4, 1):
        t.fd(size + 1)
        t.left(90)

        size -= 2
    size += 2


t.done()