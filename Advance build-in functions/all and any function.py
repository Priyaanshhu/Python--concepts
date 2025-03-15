# any and all function

# Any Function
# The any function returns True if at least one element of an iterable (such as a list, tuple, or string) is true. If all elements are false, it returns False.

numbers = [1, 2, 3, 0, 6]

result = any(num > 4 for num in numbers)
print(result) 


# All Function
# The all function returns True if all elements of an iterable are true. If at least one element is false, it returns False.

numbers = [1, 2, 0, 4, 5]

result = all(num > 0 for num in numbers)
print(result) 
