# enumerate() function 

# enumerate is a built-in function that allows you to loop over a sequence (such as a list, tuple, or string) and have access to both the index and the value of each element.

my_list = ['abc', 'xyz', 'mno']

for pos, value in enumerate(my_list):
	print(f"{pos} -----> {value}")

