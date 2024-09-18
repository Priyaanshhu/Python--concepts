# find and replace method

# find() and replace() methods are used to search and manipulate strings.


# Find Method : string.find(substring, start, end)
# - Returns the index of the first occurrence of substring in string.
# - Returns -1 if substring is not found.

my_string = "Prerna is a good girl she's even written a book"

print(my_string.find("is"))
print(my_string.find("'"))
print(my_string.find("a",15))


# Replace Method : string.replace(old, new, count)
# - Replaces old substring with new substring in string.
# - Optional count parameter specifies number of replacements.

my_string = "Rohan is a very good guy"
print(my_string.replace(" ","_"))
print(my_string.replace(" ","_", 3))
print(my_string.replace("is","was"))
