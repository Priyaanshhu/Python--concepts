# strings are immutable (unchanged)

my_string = "Pomegranate"

# This will raise a TypeError because strings in Python are immutable
# my_string[1] = "m" 
print(my_string)  

# Replace all occurrences of "g" with "b" in my_string and print the result
# Note that this doesn't modify the original string, but returns a new one
print(my_string.replace("g","b"))

# Print the original string again to demonstrate it wasn't modified
print(my_string) 
