# Exercise 5

# Ask user his name print every character of his given name and how many times a character is repeating in name print that also
# note: if there is any simliar character in name then it should not be printed again 

name = input("Enter your name : ")
temp_var = ""
i = 0
  
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} = {name.count(name[i])}")
    i = i + 1
    