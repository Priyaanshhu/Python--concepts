# Exercise 1

# define a function that take a list of strings. list containing reverse of every string
 
# user list comprehension, using normal method

# Example :
# l = ['abc', 'tuv', 'xyz']
# reverse_string ---> ['cba', 'vut', 'zyx']

def reverse_string(l):
	return [name[::-1] for name in l]
	
print(reverse_string(['abc', 'tuv', 'xyz']))
