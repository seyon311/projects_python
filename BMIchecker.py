height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi}")

if bmi < 18.4:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You're healthy.")
elif 25 <= bmi < 29.9:  
    print("You are overweight.")
elif 30 <= bmi < 34.9:
    print("You are severely overweight.")
elif 35 <= bmi < 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")                