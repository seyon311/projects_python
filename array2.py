import array as arr

array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array:", str(array_num))

print("Number of occurrences of 3 in the array:", array_num.count(3))

array_num.reverse()
print("Array after reversing:", str(array_num))