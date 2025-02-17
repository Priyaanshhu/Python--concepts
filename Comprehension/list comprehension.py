# list comprehension

# comprehension is a concise way to create list, dictionaries or sets

# normal way to create a list
square = []
for i in range(1,10):
	square.append(i**2)
print(square)
	
# comprehension way on the above list
square2 = [i**2 for i in range(1,10)]
print(square2)