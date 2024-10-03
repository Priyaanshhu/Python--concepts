# Exercise 3

# print the every item reverse in the given list using function 
# ['abc', 'mno', 'xyz'] => ['cba', 'onm', 'zyx']

def list_item(I):
    new_list = []
    for i in I:
        new_list.append(i[::-1])
    return new_list
    
user = ['abc', 'mno', 'xyz']
print(list_item(user))
    