# Exercise 1

# Ask 2 number from user and print which value is greater

def numpara(num1,num2):
    if (num1>num2):
        return(f"{num1} is greater than {num2}")
    return(f"{num2} is greater than {num1}")  
    
value1 = int(input("Enter first number : "))
value2 = int(input("Enter second number : "))
print(numpara(value1,value2))
