# center method

# The center() method in Python centers a string within a specified width.

# Syntax: string.center(width, fillchar)

# Parameters:
# - string: The input string.
# - width: The desired width of the output string.
# - fillchar (optional): The character to fill the empty space (default is space).

# Return Value:
# - A new string centered within the specified width.

# Tips:
# 1. width must be greater than or equal to the length of the string.
# 2. Use center() to format text output.
# 3. Specify fillchar to customize the filling character.


# Example 1 : 

my_string = "Pomegranate"
print(my_string.center(15, "*"))

# Example 2 :

user_name = input("Enter your name : ")
print(user_name.center(len(user_name) + 8, "*"))
