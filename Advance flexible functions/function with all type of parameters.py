# function with all type of parameters

# PADK
# P = normal paramter
# A = *args
# D = default paramter
# K = **kwargs

def my_func(word, *args, name = "Roye", **kwargs):
	print(word)
	print(args)
	print(name)
	print(kwargs)
	
my_func("apple",1,2,3,4,a = 23, b = "yep")