# string concatenation 

# String concatenation in Python is the process of combining two or more strings into a single string.

# Methods of String Concatenation:

# 1) Using the '+' operator

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  


# 2) Using the 'join()' method

str1 = "Hello"
str2 = "World"
result = " ".join([str1, str2])
print(result)


# 3) Using f-strings (formatted string literals)

str1 = "Hello"
str2 = "World"
result = f"{str1} {str2}"
print(result) 

# 4) Using the '%' operator

str1 = "Hello"
str2 = "World"
result = "%s %s" % (str1, str2)
print(result)

# 5) Using the 'format()' method

str1 = "Hello"
str2 = "World"
result = "{} {}".format(str1, str2)
print(result) 


# Best Practices:
# - Use the '+' operator for simple concatenations.
# - Use the 'join()' method for concatenating multiple strings.
# - Use f-strings for more complex string formatting.
# - Avoid using the '%' operator and 'format()' method for new code.

# Additional Tips:
# - You can concatenate strings with other data types by converting them to strings using 'str()'.
# - String concatenation creates a new string object, it does not modify the original strings.


# Additional :
# You can multiply string by (*)

str1 = "Hello World "
print(str1 * 5)
  