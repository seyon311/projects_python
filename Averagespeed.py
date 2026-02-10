a = int(input("Enter value number 1:  "))
b = int(input("Enter value number 2 ( MUST BE DIFFERENT FROM 1 ):  "))
c = int(input("Enter value number 3 (MUST BE DIFFERENT FROM 1 AND 2):  "))

avg = (a + b + c) / 3
print("The average is ", avg)

if  avg > a and avg > b and avg > c:
    print("The average is greater than all three numbers.")
elif avg > a and avg > b and avg < c:
    print("The average is greater than a and b but less than c.")
elif avg > a and avg < b and avg > c:
    print("The average is greater than a and c but less than b.")
elif avg > a and avg < b and avg < c:
    print("The average is greater than a but less than b and c.")
elif avg < a and avg > b and avg < c:
    print("The average is less than a but greater than b and less than c.")
elif avg < a and avg < b and avg > c:
    print("The average is less than a and b but greater than c.")
elif avg < a and avg < b and avg < c:
    print("The average is less than all three numbers.")               
else:
    print("The average is equal to at least one of the numbers entered.")
