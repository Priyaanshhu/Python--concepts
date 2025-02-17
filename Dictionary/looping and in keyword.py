# looping and in keyword in dictionary

user = {
    'name' : 'Prinsh',
    'age' : 25,
    'fav_movies' : ['ship', 'land on the sea'],
    'fav_food' : ['italian', 'chinese']
}

# check if key exist in dictionary 
if 'age' in user:
    print("age is exist")
else :
    print("age is not exist")
    
# check if value exist in dictionary
if 25 in user.values():
    print("25 is exist")
else :
    print("25 is not exist")

# loops in dictionary
for i in user: #for keys
    print(i)
    
for i in user.values(): #for values
    print(i)

# items() method is used with dictionaries to return a view object that displays a list of a dictionary's key value tuple pairs. you can loop through these pairs using a for loop to access both the keys and values of the dictionary
for key, value in user.items():
    print(f"The key is {key} and the values is {value}")
