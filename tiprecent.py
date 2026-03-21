def total_bill (bill_amount, tip_percentage):
    total = bill_amount + (bill_amount * tip_percentage / 100)
    print(f"Please pay £{total}")

bill_amount = float(input("Enter the bill amount: "))
tip_percentage = float(input("Enter the tip percentage: "))

total_bill(bill_amount, tip_percentage)