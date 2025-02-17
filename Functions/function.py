# function

# a function is a block of code that can be executed multiple times with different inputs. Functions are useful for:
# 1. Organizing code
# 2. Reducing repetition
# 3. Improving readability
# 4. Enhancing reusability

# Basic Function Syntax:
# def function_name(parameters):
     # code to be executed


#Example 1:

# creating a function 
def namecall(name):
    print("Hello, " + name + "!!")

username = input("Enter your name : ")
# using function 
namecall(username)  

# Example 2: 
 
#creating function  
def addingvalue(value1,value2): 
  return(value1 + value2)
  
num1 = int(input("Enter first number : "))  
num2 = int(input("Enter second number : "))  
# using function
print(addingvalue(num1,num2)) 
