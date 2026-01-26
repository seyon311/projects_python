temptype = input("Is the temperature in Celsius or Fahrenheit? (C/F): ")

if temptype.upper() == "F":
    temp = float(input("Enter the temperature in Fahrenheit: "))
    temp = (temp - 32) * 5/9
else:
    temp = float(input("Enter the temperature in Celsius: "))

if temp < 15:
    print("It's quite cold outside. Wear a jacket with a fleece and Corduroy Pants!")
elif temp > 14 and temp < 25:
    print("The weather is mild. A light sweater and Linen drawstring pants should be fine.")   
elif temp > 24 and temp < 35:
    print("It's warm outside! A T-shirt and Cotton shorts are perfect for this weather.")  
else:
    print("It's really hot! Stay cool with a Tank top and light coloured loose-fitting silhouette shorts.")  

yesno = input("Do you want to try again? (Y/N): ")

if yesno.upper() == "Y":
    exec(open("summertime.py").read())
else :
    print("Thank you for using the outfit recommender!")




