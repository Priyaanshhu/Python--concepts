# iterable and iterator

# iterable is an object that can be looped over, such as a list, tuple, string, or dictionary. An iterable is essentially a container that holds a collection of values.

# iterator is an object that keeps track of its position in an iterable and returns the next value in the sequence each time it is called.

# key difference:
	
# An iterable is the container itself (e.g., a list or string).
# An iterator is the object that helps you iterate over the container (e.g., a pointer to the current position in the list).

# Think of it like reading a book:
	
# - The book is the iterable (the container of words).
# - The bookmark is the iterator (the object that keeps track of your position in the book).

my_list = [1, 2, 3, 4, 5]  # iterable
my_iter = iter(my_list)  # create an iterator

print(next(my_iter)) 
print(next(my_iter)) 
print(next(my_iter)) 
