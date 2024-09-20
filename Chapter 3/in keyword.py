# in keyword 

# The 'in' keyword in Python is used to:
# 1. Check membership in a sequence (e.g., list, tuple, string).
# 2. Iterate over a sequence.
# 3. Check keys in a dictionary.


# Syntax:

# Membership testing:
# 'value in sequence'

# Iteration:
# 'for variable in sequence:'

# Dictionary key check:
# 'key in dictionary'


# Operators:
# - 'in' (membership testing)
# - 'not in' (non-membership testing)

# Return values:
# - 'True' (if value is in sequence or key is in dictionary)
# - 'False' (otherwise)


# Example 1: 
name = "Pratikesh"

if "a" in name:
    print("Heyy 'a' is present in your name")
else:
    print("Heyy!! 'a' is not present in your name")  

# Example 2: 
name = input("Enter your name : ")

for i in name:
    print(i)
    