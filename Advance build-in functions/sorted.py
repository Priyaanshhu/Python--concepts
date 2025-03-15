# The sorted function in Python returns a new sorted list from the elements of any sequence.

# Syntax: sorted(iterable, key=None, reverse=False)

numbers = [6, 3, 9, 1, 8, 4, 7]
sorted_numbers = sorted(numbers)
print(sorted_numbers) 


# Sorting in Descending Order:

numbers = [6, 3, 9, 1, 8, 4, 7]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers) 

# Sorting a List of Strings:

fruits = ['banana', 'apple', 'cherry', 'date']
sorted_fruits = sorted(fruits)
print(sorted_fruits) 

# Sorting a List of Dictionaries:

people = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 20}]
sorted_people = sorted(people, key=lambda x: x['age'])
print(sorted_people)  
