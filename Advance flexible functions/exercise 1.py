# define a function where take a normal parameter and args 
# square the args values by normal paramater value, do this by using comprehension method

def to_power(num, *args):
	if args:
		return [i**num for i in args]
	else:
		print("You didn't pass any args")

value = [2,2,3,4,7,5]
print(to_power(*value))