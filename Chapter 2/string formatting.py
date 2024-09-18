# string formatting 

# String formatting in Python is the process of inserting values into a string. There are several ways to format strings in Python:


# 1. Percentage Operator (%):

name = "Ravish"
age = 25
print("My name is %s and I'm %d years old." % (name, age))

# 2. String Format Method (.format()):

name = "Ravish"
age = 25
print("My name is {} and I'm {} years old.".format(name, age))

# 3. F-Strings (Formatted String Literals): 

name = "Ravish"
age = 25
print(f"My name is {name} and I'm {age} years old.")

# Formatting Options:
# - %s: String
# - %d: Integer
# - %f: Float
# - %.2f: Float with two decimal places
# - {}: Placeholder for .format()
# - {:.2f}: Float with two decimal places for .format()

# Tips:
# 1. Use f-strings for Python 3.6+.
# 2. Use .format() for older Python versions.
# 3. Avoid using the % operator.
# 4. Use formatting options for precise control.
