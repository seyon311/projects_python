fruits = ["apple", "banana", "orange"]

print(fruits[0]) # Output: apple
print(fruits[1]) # Output: banana
print(fruits[2]) # Output: orange

fruits.append("grape")
print(fruits) # Output: ['apple', 'banana', 'orange', 'grape']

fruits.remove("banana")
print(fruits) # Output: ['apple', 'orange', 'grape']

fruits[1] = "kiwi"
print(fruits) # Output: ['apple', 'kiwi', 'grape']

fruits.insert(1, "banana")
print(fruits) # Output: ['apple', 'banana', 'kiwi', 'grape']

fruits.pop(2)
print(fruits) # Output: ['apple', 'banana', 'grape']

fruits.clear()
print(fruits) # Output: []

fruits1 = ["apple", "banana", "orange"]
fruits2 = ["grape", "kiwi"]

fruits1.extend(fruits2)
print(fruits1) # Output: ['apple', 'banana', 'orange', 'grape', 'kiwi']

numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers) # Output: [1, 1, 3, 4, 5, 9]

print(min(numbers)) # Output: 1
print(max(numbers)) # Output: 9

numbers.reverse()
print(numbers) # Output: [9, 5, 4, 3, 1, 1]
