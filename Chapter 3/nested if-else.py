# nested if-else

# Nested if-else statements are used to check multiple conditions and execute different blocks of code based on those conditions.
# By using nested if-else statements effectively, you can write more complex decision-making logic

# Syntax:

# if condition1:
    #if condition2:
        # code to execute if both conditions are true
    #else:
        # code to execute if condition1 is true and condition2 is false
#else:
    #if condition3:
        # code to execute if condition1 is false and condition3 is true
    #else:
        # code to execute if condition1 is false and condition3 is false


age = int(input("Enter your age : "))

if age >= 18:
  income = int(input("Enter your income : "))
  if income >= 40000: 
    print("You're eligible for loan")
  else: 
    print("You're income is under 40k not eligible for laon")
else: 
  print("You're under 18 not eligible for loan")
  