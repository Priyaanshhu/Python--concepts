# *args with normal parameter

def multiply_nums(num,*args): #(normal parameter, *args)
	print(num)
	print(args)
	multiply = 1
	for i in args:
		multiply *= i
	return multiply
	
print(multiply_nums(6,2,3,5,3))
