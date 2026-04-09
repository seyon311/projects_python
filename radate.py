import random
again = True

while again:
    year = random.randint(1900, 2026)
    month = random.randint(1, 12)
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:  # February
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            day = random.randint(1, 29)  # Leap year
        else:
            day = random.randint(1, 28)

    print(f"Random Date: {day}/{month}/{year}")   

    again_input = input("Again? (Y/N): ").strip().upper()
    if again_input == 'Y':
        again = True
    else:
        again = False

print("Thank you for using the program!")        
