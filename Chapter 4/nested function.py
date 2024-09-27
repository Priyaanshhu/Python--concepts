# nested function 

# function inside function is called nested function 

def personal_details():
    def print_details(name, age, salary):
        return f"Heyy!! I'm {name} and my age is {age}, my salary is {salary}k."

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    salary = int(input("Enter your salary: "))
    print(print_details(name, age, salary))

personal_details()
