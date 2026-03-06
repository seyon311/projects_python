number = int(input("Enter a number: "))

count = 0
n = abs(number)
while n > 0:
    count += 1
    n = n // 10
print(count)