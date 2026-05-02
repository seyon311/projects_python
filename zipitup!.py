s1 = {2, 3, 1}
s2 = {'a', 'b', 'c'}

print("First set:", s1)
print("Second set:", s2)

result = zip(s1, s2)
print("Zipped sets:", list(result), "\n")

l1 = [10, 20, 30, 40]
l2 = [100, 200, 300, 400]

print("First list:", l1)
print("Second list:", l2)

for x, y in zip(l1, l2[::-1]):
    print(f"Zipped values: {x} and {y}\n")

stocks = ["reliance", "tata", "infosys"]
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}

print("Stock prices dictionary:", new_dict)