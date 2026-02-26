string = str(input("\nEnter a string which you want to reverse: "))

if string == "":
    print("The string is empty.")
else:
    reversed_string = ""

    for i in string:
        reversed_string = i + reversed_string

    print(f"\nThe original string is: {string}")
    print(f"The reversed string is: {reversed_string}")    