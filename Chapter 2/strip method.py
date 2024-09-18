# strip method()

# The strip() method in Python removes leading and trailing characters (whitespace by default) from a string.

# Syntax: string.strip([chars])

# Parameters:
# - string: The input string.
# - chars (optional): Characters to remove (default is whitespace).

# Return Value:
# - A new string with leading and trailing characters removed.

# Variations:
# - lstrip(): Removes leading characters only.
# - rstrip(): Removes trailing characters only.


# Example 1 :
  
my_string = "       Pomegranate        "
dots = "..........."

print(my_string.lstrip() + dots)
print(my_string.rstrip() + dots)
print(my_string.strip() + dots)

# Example 2 :

my_string = "#######Pomegranate########"
dots = "............."

print(my_string.lstrip("#") + dots)
print(my_string.rstrip("#") + dots)
print(my_string.strip("#") + dots)
