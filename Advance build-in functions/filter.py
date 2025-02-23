# filter() function

# filter function is a built-in function that takes a function and an iterable (such as a list, tuple, or string) as arguments, and returns a new iterable that contains only the items for which the function returns True.

# syntax for the filter function is:
# filter(function, iterable)

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6,7,8,9]

even_numbers = list(filter(is_even, numbers))
print(even_numbers) 