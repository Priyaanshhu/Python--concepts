# kwargs (keyword argument)
# **kwargs (double star operator)

# when you define a function with **kwargs as a parameter, it allows you to pass any number of keyword arguments to the function. These arguments are collected into a dictionary called kwargs.

def myfunc(**kwargs):
	for k,v in kwargs.items():
		print(f"{k}:{v}")
	print(type(kwargs))
		
myfunc(name = "Joy", surname = "Roe")
