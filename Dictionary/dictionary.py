# Dictionary

# A dictionary is unordered collections of data in key : value pair
# There is no indexing because of unordered collections of data

# how to create dictionary
user = {
	'name' : 'Rajin', 
	'age' : 24
} 
print(user)
print(type(user))

# another method to create dictionary
user1 = dict(name = 'Rajin', age = 24)
print(user1)

# access data from dictionary
print(user['name'])
print(user['age'])
print(user1['name'])

# adding data to empty dictionary
user2 = {}
user2['name'] = 'Rajin'
user2['age'] = 24
print(user2)
