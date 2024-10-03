# Evercise 5

# Make function where you take two list them compare them and print the common numbers between them

def simliar_find(l1,l2):
    new_list = []
    for i in l1:
        if i in l2:
            new_list.append(i)
    return new_list        

list_one = [1,2,3,4,5,6,7]
list_two = [0,3,9,4,8,2]
print(simliar_find(list_one,list_two))
