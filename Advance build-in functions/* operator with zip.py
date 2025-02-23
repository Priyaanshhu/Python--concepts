# * operator with zip

my_list = [(2,4), (7,8), (9,3), (6,1)]

value1,value2 = list(zip(*my_list))
print(value1)
print(value2)