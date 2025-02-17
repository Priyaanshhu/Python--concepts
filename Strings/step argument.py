# step argument 

# The step argument in string slicing in Python is an optional parameter that specifies the increment between indices.

# Step Argument Options:
# 1. Positive Step: Extracts every step-th character.
# 2. Negative Step: Extracts every step-th character in reverse order.
# 3. Step = 1 (default): Extracts consecutive characters.

# Common Use Cases:
# 1. Extracting every nth character.
# 2. Reversing a string.
# 3. Creating substrings with specific intervals.

# Tips:
# 1. Omitting step defaults to 1.
# 2. Negative step reverses the string.
# 3. step can be any integer.

# Additional Examples:
# - Extracting every 2nd character: mystring[::2]
# - Extracting every 3rd character in reverse: mystring[::-3]
# - Reversing a string with step 2: mystring[::-2]
# Syntax: string[startindex:endindex:step]


# Positive Step : 

mystring = "Pomegranate"
print(mystring[::3]) 
print(mystring[2:10:2])  

# Negative Step : 
  
mystring = "Pomegranate"
print(mystring[::-1])  
print(mystring[::-2])  #

# Step = 1 (default) : 

mystring = "Pomegranate"
print(mystring[::1]) 

# Reverse string :
  
mystring = "Pomegranate"
print(mystring[::-1]) 
print(mystring[-1::-1]) 
