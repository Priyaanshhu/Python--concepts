# list comprehension in nested list

# without comprehension nested list
new_list = []
for i in range(3):
	new_list.append([1,2,3])
print(new_list)

# with comprehension nested list
nested_comp = [[i for i in range(1,4)] for j in range(3)]
print(nested_comp)