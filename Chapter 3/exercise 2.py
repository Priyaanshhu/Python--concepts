# Exercise 2

# Ask user a name and age and if he have "a" or "A" in his name first character and if he's age is above or equal to 10 then print "Heyy!! You can watch CoCo movie" else print "Sorry!! You cannot watch CoCo movie"

name = input("Enter your name : ")
  age = int(input("Enter you age : "))
  
  if (name[0] == "A" or name[0] == "a") and age >= 10:
    print("Heyy!! You can watch CoCo movie")
  else: 
    print("Sorry!! You cannot watch CoCo movie")
    