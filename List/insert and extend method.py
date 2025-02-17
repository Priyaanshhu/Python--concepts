# insert and extend method 

# the insert() and extend() methods in Python lists:


# Insert Method:

# Syntax: listname.insert(index, element)
# Purpose: Inserts a single element at a specified index.


fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "grape")
print(fruits) 

# Key Points:
# 1. Index: Specify the position where the element will be inserted (0-based)
# 2. Element: Can be of any data type
# 3. Shifts existing elements to the right


# Extend Method:

# Syntax: listname.extend(iterable)
# Purpose: Adds multiple elements from an iterable


fruit1 = ["apple", "banana"]
fruit2 = ["cherry", "mango"]
fruit1.extend(fruit2)
print(fruit1)]

# Key Points:
# 1. Adds all elements from the iterable.
# 2. Efficient for adding multiple elements.
