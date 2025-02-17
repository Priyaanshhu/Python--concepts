# Exercise 1

# define a function that takes a number(n) and return a dictionary containing cube of numbers from 1 to n
# eg. cube finder(3)
#		{1:1, 2:8, 3;27} 

def cube_finder(n):
	cubes = {}
	for i in range(1,n+1):
		cubes[i] = i**3
	return cubes

print(cube_finder(5))