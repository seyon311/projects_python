numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7, 8]

print("First list:", numbers1)
print("Second list:", numbers2)

result = map(lambda x, y: x + y, numbers1, numbers2)
print("Addition of both lists:", list(result), "\n")

nums = [1, 2, 3, 4, 5]
print("Original list: ", nums)

def square(x):
    return x**2

nums_squared = list(map(square, nums))
print("Square of number in list: ", nums_squared)
