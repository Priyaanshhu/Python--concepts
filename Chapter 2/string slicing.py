# string slicing 

# String slicing in Python allows you to extract a subset of characters from a string.

# Syntax: string[start index : end index]

# Parameters:
# 1. start index: The starting index of the slice (inclusive).
# 2. end index: The ending index of the slice (exclusive).

# Basic Slicing : 

my_string = "Pomegranate"
print(my_string[0:5])  
print(my_string[7:11]) 

# Omitting Start or End Index : 

my_string = "Pomegranate"
print(my_string[:5])
print(my_string[8:])  

# Negative Indexing

my_string = "Pomegranate"
print(my_string[-5:])  
print(my_string[-5:-2])  

# Note :
# 1. Omitting start index starts from 0.
# 2. Omitting end index goes to the end of the string.
# 3. Negative indexing starts from -1.
