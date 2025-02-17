# for loop

# The for loop is used to iterate over a sequence and execute a block of code for each item.

# Syntax:
#  for variable in iterable:
     # code to execute

# Components:
# 1. Variable: Takes on the value of each item in the iterable.
# 2. Iterable: The sequence to iterate over.
# 3. Body: The code executed for each item.


#Example 1:

for i in range(5):
  print(i)

#Example 2:

for var in range(1, 11):
  print(f"Hello World {var}")

#Example 3:

num = input("Enter numbers to sum : ")
total = 0

for i in range(0, len(num)):
    total += int(num[i])
    i += 1
print(total) 

#Example 4:

name = input("Enter your name to get number of each character in your name : ")
var = ""

for i in range(len(name)):
    if name[i] not in var:
        print(f"{name[i]} = {name.count(name[i])}")
        var += name[i]
        