a = str(input("Enter a string: "))

for i in a:
    if i == "a":
        print("Found an a!")
        break
    else:
        print(f"{i} is not an a.")