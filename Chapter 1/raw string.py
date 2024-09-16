# raw string

# a raw string is a string literal that treats backslashes ('\') as literal characters, rather than escape characters. This means that raw strings do not interpret escape sequences, such as '\n' for newline or '\t' for tab.

# To create a raw string, prefix the string with 'r' or 'R', like this

# "This is a raw string"
# raw_string = r 

# In a raw string:
# - Backslashes are treated as literal characters, not escape characters.
# - No escape sequences are interpreted.
# - The string is taken as-is, without any processing.

# Note that raw strings can still contain Unicode characters, and the 'r' prefix only affects the treatment of backslashes.

# Example 1 :
print(r"C:\Windows") 

# Example 2 :
  print(r"Hello I'm a raw string and \n")
 