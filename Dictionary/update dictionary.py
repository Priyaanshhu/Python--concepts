# update dictionary

# update method is used to update the contents of a dictionary by adding elements from another dictionary

user_info = {
    'name' : 'Moksh'
}

more_info = {
    'age' : 27
}

user_info.update(more_info)
print(user_info)