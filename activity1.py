x = 5

if type(x) is int:
    print("x is an integer")
else:
    print("x is not an integer")

x = 5.5

if type(x) is float:
    print("x is a float")
else:
    print("x is not a float")

x = 20
y = 20

if x is y:
    print("x and y reference the same object")
else:
    print("x and y reference different objects")

y = 30

if x is not y:
    print("x and y reference different objects after changing y")