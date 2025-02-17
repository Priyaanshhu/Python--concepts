# default parameter

# default parameters allow you to specify a value for a function parameter that will be used if no value is provided when the function is called.

# Syntax:

# def function_name(parameter1=default_value, parameter2=default_value):
    # function body

# Key Points:
# 1. Default parameters must come after non-default parameters.
# 2. Default values are evaluated only once at the time of function definition.
# 3. Default parameters can be mutable

  
# Example 1:

def greet(name="unknown"):
    print(f"Hello, {name}!")

greet()  
greet("Richard")  
