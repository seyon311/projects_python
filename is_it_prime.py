lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

print(f"Prime numbers between {lower} and {upper} are:")

if lower < 2:
    lower = 2

for num in range(lower, upper + 1):

    if num > 1:
        
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
                
            print(num)

                