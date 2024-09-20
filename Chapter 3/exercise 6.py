# Exercise 6

# Assign a winning number and ask user to guess a number if guessing number is lower than winning number then print to low then ask again input a number and guessing number is higher than winning number then print to high then ask again to input a number and if user guess right number then print you win 
# if user win then exit the game (game over)

winning = 36
num = int(input("Guess a number between (1 - 50) : "))
guess = 1
game_over = False
      
while not game_over : 
  if num == winning : 
    print(f"Youu Winn !! while guessing number in {guess} times")
    game_over = True
  else : 
    if num < winning : 
      print("Too Low")
      guess += 1
      num = int(input("Guess again : "))
    else : 
      print("Too High")
      guess += 1
      num = int(input("Guess again : "))
            