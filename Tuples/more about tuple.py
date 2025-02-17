# More about tuple 

# 1) Looping in tuple

mixed = (1,2,3,4,5)
for i in mixed:
  print(i)
  
# 2) tuple with one element 

tup = (1,)
print(tup)

# 3) tuple without parenthesis 

mixed = 1,2,3,4,5
print(mixed)

# 4) tuple unpacking 

hero = ("superman", "spiderman", "batman", "ironman")
mickey, oggy, ben, hattori = (hero)
print(oggy)

# 5) list inside tuple 

name = ('sivir', ['josh', 'elina'])
name[1].pop()
name[1].append('you are change')
print(name)

# some function inside tuple : min,max,sum

mixed = (1,2,4,3,6,5,8,7,9)
print(min(mixed))
print(max(mixed))
print(sum(mixed))

    