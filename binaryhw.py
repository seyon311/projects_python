n = int(input("\nEnter a integer: "))
binary = []

while n > 0:
    binary.append(n % 2)
    n = n // 2

binary.reverse()

print("Binary representation: ", end="")

for i in binary:
    print(i, end="")

print("\n")
