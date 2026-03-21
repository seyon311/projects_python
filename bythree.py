def cube(n):
    return n**3

def bythree(n):
    if n % 3 == 0:
        return f"{cube(n)} is a multiple of three"
    else:
        return f"{n} is not a multiple of three"

number = int(input("Enter a number: "))
print(bythree(number))    