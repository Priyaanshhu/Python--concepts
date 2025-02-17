# * operator/ * args

# *args is a special syntax used to pass a variable number of arguments to a function. It allows a function to accept any number of additional arguments beyond what is explicitly defined in the function signature.

def total(*args):
	total = 0
	for num in args:
		total += num
	return total
print(total(1,2,3,4,5,6,7,8,9))
