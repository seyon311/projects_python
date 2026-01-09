print("Enter marks obtained in 4 subjects:")

math = int(input("Math : "))
science = int(input("Science : "))
history = int(input("History : "))
english = int(input("English : "))

total = math + science + history + english
print("Sum of Maths, Science, History and English marks is:", total)
percentage = (total / 400) * 100
print("The percentage is:", percentage)
average = total / 4
print("The average marks is:", average)