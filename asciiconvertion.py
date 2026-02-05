# Get input from user

char = input("Enter a single character: ")


# Validate: Check if exactly one character

if type(char) is str and len(char) == 1:

    print("Valid input!")

else:

    print("Please enter exactly ONE character!")

# Get ASCII value

ascii_val = ord(char)


# Display the result

print(f"Character: {char}")

print(f"ASCII Value: {ascii_val}")

# Identify character type using ASCII ranges

if ascii_val >= 65 and ascii_val <= 90:

    print("Type: Uppercase Letter")

elif ascii_val >= 97 and ascii_val <= 122:

    print("Type: Lowercase Letter")

elif ascii_val >= 48 and ascii_val <= 57:

    print("Type: Digit")

elif ascii_val == 32:

    print("Type: Space")

else:

    print("Type: Special Character")