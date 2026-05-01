my_set = {1, 2, 3} # This is a set of integers
print(my_set) # Output: {1, 2, 3}

my_set = {1.0, "Hello", True, (1, 2)} # This is a set with different data types
print(my_set) # Output: {1.0, 'Hello', True, (1, 2)}

my_set = {1, 3, 3, 2, 4} # This set will only contain unique elements
print(my_set) # Output: {1, 2, 3, 4} prints in sorted order, but the actual order in the set may vary

# Set from a list

my_set = set([1, 2, 3, 4, 5])
print(my_set, "\n")

num_set  = set([1, 0, 2, 3, 4, 5, 4])
print("Original set:", num_set) # Output: {0, 1, 2, 3, 4, 5} because set automatically removes duplicates and does not maintain order
num_set.pop() # Removes and returns an arbitrary element from the set
print("Set after pop:", num_set)

