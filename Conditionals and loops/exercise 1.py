# Exercise 1 

# Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number
# if user guessed correctly then print "YOU WIN !!!!"
# if user didn't guessed correctly then:
  #if user guessed lower than actual number then print "too low"
  #if user guessed higher than actual number then print "too high"
  
winning_number = 17
guess_num = int(input("Guess a number between 1 to 30 : "))

if winning_number == guess_num: 
  print("YOU WIN !!!!")
else: 
  if winning_number > guess_num: 
    print("Too Low")
  else: 
    print("Too High")
    