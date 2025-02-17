# Exercise 4

# Take a 'given' list and print the list where inside them there a odd number list and even number of the 'given' list by using function 

def odd_even(I):
    odd_num = []
    even_num = []
    for i in I:
        if i%2 == 0:
            even_num.append(i)
        else:
            odd_num.append(i)    
    output = [even_num, odd_num]
    return output

given = list(range(1,11))
print(odd_even(given))