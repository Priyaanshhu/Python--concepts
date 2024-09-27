# Variable scope

# Variable scope refers to the region of the code where a variable is defined and accessible. Python has the following variable scopes

# Python follows the LEGB rule for resolving variable scope:
# 1. Local
# 2. Enclosing
# 3. Global
# 4. Built-in

# Best Practices
# 1. Use meaningful variable names.
# 2. Avoid global variables when possible.
# 3. Use encapsulation (classes) for complex data.
# 4. Keep variable scope narrow.


# 1) Local Scope

#Variables defined inside a function or method.

def my_function():
    local_var = 10  # Local variable
    print(local_var)

my_function()  
print(local_var)  # NameError: local_var is not defined


# 2) Enclosing Scope (Nonlocal)

# Variables defined in an outer, but not global, scope.

def outer_function():
    enclosing_var = 20  # Enclosing variable

    def inner_function():
        nonlocal enclosing_var
        enclosing_var = 30
        print(enclosing_var)

    inner_function()
    print(enclosing_var)

outer_function() 


# 3) Global Scope

#Variables defined at the top level of a module.

global_var = 40  # Global variable

def my_function():
    print(global_var)

my_function()  
print(global_var)  


# 4) Built-in Scope

# Reserved variables and functions, like len(), range(), etc.

print(len([1, 2, 3])) 
