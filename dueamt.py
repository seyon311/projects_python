print("Imagine you have the pay a certain amount of money, but you only pay some of it. How much is pending?")

total_amount = float(input("Enter the total amount: "))
paid_amount = float(input("Enter the amount paid: "))

if paid_amount > total_amount:
    print("You have overpaid. Please check the amounts entered.")
elif paid_amount == total_amount:
    print("You have paid the full amount. No pending amount.")
else:
    pending_amount = total_amount - paid_amount
    print(f"The pending amount is: {pending_amount}")