try:
    number = int(input("Enter a number: "))
    print("You have entered:", number)
except ValueError as ex:
    print("Exception occurred:", ex)    