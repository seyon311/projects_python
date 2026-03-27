int = int(input("Enter a number: "))

for i in range (1, int + 1):
    if i % 20 == 0:
        if i % 3 == 0:
            print("TwistFizz")
        elif i % 5 == 0:
            print("TwistBuzz")
        else:
            print("Twist")
    elif i % 15 == 0:
        pass
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
