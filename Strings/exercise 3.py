# Exercise 3

# take two comma separated inputs from user his "user name" and a "single character"
# print username length and count the taken single character in username (this should be case insensitive count) and print 

user_name, sing_char = input("Enter your name and a single character of you name (John n) : ").split()

print(f"Your name length is : {len(user_name)}")
print(f"This single character repeat {user_name.lower().count(sing_char.lower())} time in your name")
