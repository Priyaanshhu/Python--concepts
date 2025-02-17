# print vs return 

# 'print' and 'return' serve different purposes:

# Print:
# 1. Outputs text or values to the console or standard output.
# 2. Primarily used for debugging, logging, or displaying information.
# 3. Does not affect the function's return value.

# Return:
# 1. Specifies the output value of a function.
# 2. Ends the function's execution.
# 3. Allows the function to provide a result to the caller.

# When to use each:
# - Use 'print' for:
#     - Debugging
#     - Logging
#     - Displaying information
# - Use 'return' for:
#     - Calculating values
#     - Processing data
#     - Providing output to the caller

# Best practices:
# - Use 'print' sparingly in production code.
# - Prefer 'return' for functions that calculate or process data.
# - Use 'print' in interactive shells or debugging sessions.

# Example (print): 
def addingvalue(value1,value2): 
  print(value1 + value2)
  
num1 = int(input("Enter first number : "))  
num2 = int(input("Enter second number : "))  
(addingvalue(num1,num2)) 


# Same example using (return): 
def addingvalue(value1,value2): 
  return(value1 + value2)
  
num1 = int(input("Enter first number : "))  
num2 = int(input("Enter second number : "))  
print(addingvalue(num1,num2)) 
