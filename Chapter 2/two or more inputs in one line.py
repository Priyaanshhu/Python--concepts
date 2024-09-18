# two or more inputs in one line

# Taking two input in one line by using 'split()' method 
# split() method will seperate the input into two string and stored them in given variable respectively 

# Example 1:
name, age = input("Enter your name and age (Monika 21) : ").split()
print(name, age)

# Example 2: 
name, age, hobby = input("Enter your name, age and hobby (Monika 21 drawing) : ").split()
print(name, age, hobby)
