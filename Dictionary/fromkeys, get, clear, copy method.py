# fromkeys, get, clear, copy method

# fromkeys() is used to create a new dictionary with specified keys and values
# syntax: dict.fromkeys(keys, value)
user = dict.fromkeys(['name', 'age', 'education'], 'unknown') 
print(user)

# get() method is used to retrieve the value of a key from a dictionary. it returns the value for the given keys if it exists in the dictionary. if the key does not exist, it returns a default value.
# syntax: dict.get(key, default=None)
user1 = {
    'name' : 'mokshita',
    'age': 25
}
print(user1.get('age'))
print(user1.get('occupation'))

# clear() is used to clear values
user1.clear()
print(user1)

# copy() is used to copy dictionary
new_user = user.copy()
print(new_user)
