# Exercise 2

# Ask user name,age,fav_movies and fav_songs
# add these values into dictionary
# print all values of dictionary into new line

user = {}

name = input("enter your name : ")
age = int(input("enter your age : "))
fav_fruits = input("enter your fav fruits by using comma : ").split(',')
fav_songs = input("enter your fav songs by using comma : ").split(',')

user['name'] = name
user['age'] = age
user['fav_fruits'] = fav_fruits
user['fav_songs'] = fav_songs

for key, value in user.items():
	print(f"{key} : {value}")
	
