# elif statement 

# The elif statement is used to check multiple conditions and execute different blocks of code.

# Syntax:

#if condition1:
    # code to execute if condition1 is true
#elif condition2:
    # code to execute if condition1 is false and condition2 is true
#elif condition3:
    # code to execute if condition1 and condition2 are false and condition3 is true
#else:
    # code to execute if all conditions are false


# Example 1:

grade = 85

if grade >= 90:
    print("A grade")
elif grade >= 80:
    print("B grade")
elif grade >= 70:
    print("C grade")
else:
    print("Fail")
    

#Example 2:

age = int(input("Enter your age : "))

if age <= 18:
    print("Show is free for you")
elif age <= 30:
    print("Ticket price is 250")
elif age <= 50:
    print("Ticket price is 200")    
else:
    print("Ticket price is 150")    