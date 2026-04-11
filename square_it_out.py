lower_bound = int(input("Enter a lower bound:"))
upper_bound = int(input("Enter an upper bound:"))

squares = []

for i in range(lower_bound, upper_bound + 1):
    if i ** 0.5 == int(i ** 0.5):
        squares.append(i)

even = []
odd = []

for i in squares:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("the squares between", lower_bound, "and", upper_bound, "are:", squares)
print("the odd squares between", lower_bound, "and", upper_bound, "are:", odd)
print("the even squares between", lower_bound, "and", upper_bound, "are:", even)