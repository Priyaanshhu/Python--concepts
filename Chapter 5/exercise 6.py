# Exercise 6

# Create a function where you can check how many sublist are there in list 

def list_checker(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count        

my_list = [1,2,[10,20,30],5,6,[5,8,7],[55,65,77]]
print(list_checker(my_list))
