# Exercise 2

# define a function where take a list and return a list
# while returning the list the value's first letter should be capital
#  if there is 'reverse_str == True' in the argument then reverse the every value's of list and then capitalize the first letter

def my_func(value, **kwargs):
	if kwargs.get('reverse_str') == True:
		return [name[::-1].title() for name in value]
	else:
		return[name.title() for name in value]		

my_list = ['pomegranate', 'elephant', 'peacock']
print(my_func(my_list))
print(my_func(my_list, reverse_str = True))
