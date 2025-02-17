# Exercise 2

# Ask user a palindrome word and if the word is palindrome then print "The given word is palindrome" else print "The given word is not palindrome"

username = input("Enter a palindrome(same after reversed) word like 'madam' : ")

def palindrome(mystring): 
  if username == username[::-1]: 
    print("The given word is palindrome")
  else: 
    print("The given word is not palindrome")  
    
palindrome(username) 
