print("\nThis program will swap three numbers as follows:")
print("num1 will replace num2, num2 will replace num3, and num3 will replace num1.\n")


print("Please Enter the 1st number to begin swapping: ")
num1 = int(input())
print("Enter the 2nd number to swap: ")
num2 = int(input())
print("Enter the 3rd number to swap: ")
num3 = int(input())
print("The numbers before swapping are:", num1, num2, num3)
holder = num1
num1 = num2
num2 = num3
num3 = holder       
print("The numbers after swapping are:", num1, num2, num3)