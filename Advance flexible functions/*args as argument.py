# *args as argument

def multiply_nums(*args): #(normal parameter, *args)
	print(args)
	multiply = 1
	for i in args:
		multiply *= i
	return multiply

value = (1,2,3) 		
print(multiply_nums(*value)) # *args as argument [this will unpack the tuple]
