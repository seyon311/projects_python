withdrawal = int(input("How much money do you want to withdraw? "))

notes100 = withdrawal // 100
notes50 = (withdrawal%100) // 50
notes10 = ((withdrawal%100)%50) // 10

print("Notes of $100:", notes100)
print("Notes of $50:", notes50)
print("Notes of $10:", notes10)