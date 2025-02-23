# map() function

# map function is a built-in function that applies a given function to each item of an iterable (such as a list, tuple, or string) and returns a new iterable with the results.

# The map function takes two arguments:

# 1. A function that you want to apply to each item of the iterable.
# 2. The iterable itself.

# The syntax for the `map` function is:
# map(function, iterable)

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(square, numbers))
print(squared_numbers) 
