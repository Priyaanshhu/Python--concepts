# delete data from list

# the pop(), remove(), and del methods in lists:

# Pop Method :

# Syntax: listname.pop(index)
# Purpose: Removes and returns an element at a specified index.

fruits = ["apple", "banana", "cherry"]
poppedfruit = fruits.pop(1)
print(fruits)  
print(poppedfruit) 

# Key Points:
# 1. Index: Specify the position of the element to remove (0-based).
# 2. Returns the removed element.
# 3. Raises IndexError if index is out of range.


# Remove Method :

# Syntax: listname.remove(element)
# Purpose: Removes the first occurrence of a specified element

fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits) 

# Key Points:
# 1. Element: Specify the value to remove.
# 2. Removes only the first occurrence.
# 3. Raises ValueError if element is not found.


# Del Statement :

# Syntax: del listname[index] or del listname[start:stop]
# Purpose: Removes an element or a slice of elements.

# Example 1: 
fruits = ["apple", "banana", "cherry"]
del fruits[1]
print(fruits)  

# Example 2: 
fruits = ["apple", "banana", "cherry", "date"]
del fruits[1:3]
print(fruits)  

# Key Points:]
# 1. Index or slice: Specify the position(s) to remove.
# 2. Does not return the removed element.
# 3. Raises IndexError if index is out of range.
