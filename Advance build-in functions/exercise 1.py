# Exercise 1

# add all values from a variable and if any input is string or symbol them print "Wrong input". use all function

def my_value(*args):
	if all([(type(arg) == int or type(arg) == float) for arg in args]):
		total = 0
		for num in args:
			total += num
		return total
	else:
		return "Wrong input"
	
print(my_value(1,2,3,4,6.7))