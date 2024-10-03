# Exercise 2

# Create a function where you reverse a list by using pop() and append() method

def list_item(I):
    square = []
    for i in range(len(I)):
        pop_item = I.pop()
        square.append(pop_item)
    return square
    
user = list(range(1,11))
print(list_item(user))
    