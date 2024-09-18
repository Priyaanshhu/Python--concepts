# Exercise 1

# Ask user to input 3 numbers and you have to print average of three numbers using string formatting.
# try to take all three comma separated inputs in one line

num1, num2, num3 = input("Enter your three number (1,2,3) : ").split(",")
sum_avg = (int(num1) + int(num2) + int(num3)) / 3
print(f"The average of {num1}, {num2} and {num3} is : ", int(sum_avg))
