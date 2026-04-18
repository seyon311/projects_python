tuplex = ("Hello", True, 3.14, 37)
print(tuplex)

"""
Tuples are immutable, which means that you cannot change their values after they have been created.
You can access the elements of a tuple using indexing, and you can also use slicing to get a range of elements from the tuple.
However, you cannot add, remove, or modify the elements of a tuple once it has been created. 
"""

tuple1 = (40, 20, 50, 10, 50)
print(tuple1.count(50))  # Count the number of times 50 appears in the tuple

tuple2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# Slicing follows the syntax: tuple[start:stop:step]
print(tuple2[2:5])  # Get elements from index 2 to 4 (5 is not included)
print(tuple2[::2])  # Get every second element from the tuple