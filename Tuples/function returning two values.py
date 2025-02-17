# function returning two values

def func(int1, int2):
	add = int1 + int2
	multiply = int1*int2
	return add, multiply

# This function will return value in tuple
print(func(2,3))

# seprating this tuple value 
add, multiply = func(2,3)
print(add)
print(multiply)
