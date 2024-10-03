# Exercise 1

# create a function where return square of items in list and then print them

def squarelist(I):
    square = []
    for i in I:
        square.append(i**2)
    return square
    
user = list(range(1,11))
print(squarelist(user))
    