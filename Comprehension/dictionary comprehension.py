# dictionary comprehension

# Example 1
square_num = {f"Square of {num} is": num**2 for num in range(1,11)}
for k,v in square_num.items():
	print(f"{k} : {v}")
	
# Example 2
word = "pomegranate"
word_count = {char:word.count(char) for char in word} 
for x,y in word_count.items():
	print(f"{x} : {y}")