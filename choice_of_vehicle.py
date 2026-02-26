print("\nSelect your ride: ")
print("1. Bike")
print("2. Car")
print("Enter the number corresponding to your choice: \n")

if int(input("")) == 1:
    print("\nYou have selected Bike as your ride, what type would you like to have?")
    print("1. Scooty")
    print("2. Scooter")
    print(" Enter the number corresponding to your choice: \n")

    if int(input("")) == 1:
        print("\nYou have selected Scooty as your ride.")
    elif int(input("")) == 2:
        print("\nYou have selected Scooter as your ride.")
    else:
        print("\nInvalid input. Please select a valid option.")

elif int(input("")) == 2:
    print("\nYou have selected Car as your ride, what type would you like to have?")
    print("1. Sedan")
    print("2. SUV")
    print(" Enter the number corresponding to your choice: \n")

    if int(input("")) == 1:
        print("\nYou have selected Sedan as your ride.")
    elif int(input("")) == 2:
        print("\nYou have selected SUV as your ride.")
    else:
        print("\nInvalid input. Please select a valid option.")

else:
    print("\nInvalid input. Please select a valid option.")

    
        

