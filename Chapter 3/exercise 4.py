# Exercise 4

# Ask some numbers to user and give sum of that number 
# note : don't take number as a integer take as a string and then convert it later into integer 


num = input("Enter some numbers to sum it : ")
total = 0

i = 0
while i < len(num):
    total = total + int(num[i])
    i = i + 1
print(total) 
