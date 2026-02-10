print("Enter a number (Numerator): ")
numerator = int(input())
print("Enter another number (Denominator): ")   
denominator = int(input())

if denominator == 0:
    print("Error: Denominator cannot be zero.")
else:
    if numerator % denominator == 0:
        print(f"\n  {numerator} is divisible by {denominator}.")
    else:
      print(f"\n  {numerator} is not divisible by {denominator}.") 
