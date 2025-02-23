# zip() function

# zip function is a built-in function that allows you to iterate over two or more lists (or other iterables) simultaneously.

# syntax:
# zip(iterable1, iterable2, ...)

user_id = ['user1', 'user2', 'user3']
user_name = ['Roy', 'vinie', 'tanya']
last_name = ['vis', 'matt', 'singh']

user_all = list(zip(user_id,user_name,last_name))

for i,j,k in user_all:
	print(f"{i} is {j} and the surname is {k}")
