# user input 

# input() function in Python allows you to read user input from the console. It returns a string, so if you need to convert it to another data type, you'll need to do so explicitly.
# If the user enters something that can't be converted to the desired data type, a 'ValueError' will be raised.

# Basic Syntax: input(prompt)

# Arguments:
# 'prompt': The text displayed to the user, prompting them to enter input.

your_name = input("Enter your name : ")
print("Hello, " + your_name)
