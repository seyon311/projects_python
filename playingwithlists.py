list1 = [5, 3, 1, 2, 4, 8, 9, 7, 6]


chr = 0
for i in list1:
    chr += i

print("the sum of the numbers in the list is:", chr)

length = len(list1)

print("the average of the numbers in the list is:", chr / length)

list1sorted = list1.sort()
print("the sorted list is:", list1)

print("the smallest number in the list is:", min(list1))
print("the largest number in the list is:", max(list1))
