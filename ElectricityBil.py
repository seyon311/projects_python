print("\nWelcome to the Electricity Billing System!\n")

UnitsConsumed = float(input("Enter the number of units consumed: "))

if UnitsConsumed < 0:
    print("Invalid input. Please enter a valid number for units consumed.")

else:

    if UnitsConsumed < 50.:
        PerUnit = 2.60
        Tax = 25
    elif UnitsConsumed >= 50. and UnitsConsumed < 100:
        PerUnit = 3.25
        Tax = 35
    elif UnitsConsumed >= 100. and UnitsConsumed < 200:
        PerUnit = 5.26
        Tax = 45
    else :
        PerUnit = 8.45
        Tax = 75

    Total = UnitsConsumed * PerUnit + Tax
    print(f"Your electricity bill is £{Total}. Your per unit cost was £{PerUnit} and your tax was £{Tax}.")

print("Thank you for using our electricity billing system!")
