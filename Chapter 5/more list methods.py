# more list methods

# count, sort, sorted, reverse, clear, copy


# 1. Count()
#count() returns the number of occurrences of a specified element in the list.

Number = [3,8,6,8,9,0]
print(Number.count(8))  # Output: 2


# 2. Sort()
# sort() sorts the list in-place, meaning it modifies the original list.

Number = [3,8,6,8,9,0]
Number.sort()
print(Number)  # Output: [0, 3, 6, 8, 8, 9]


# 3. Sorted()
# sorted() returns a new sorted list without modifying the original list.

Number = [3,8,6,8,9,0]
sorted_Number = sorted(Number)
print(sorted_Number)  # Output: [0, 3, 6, 8, 8, 9]
print(Number)  # Original list remains unchanged: [3, 8, 6, 8, 9, 0]


# 4. Reverse()
# reverse() reverses the order of the list in-place.

Number = [3,8,6,8,9,0]
Number.reverse()
print(Number)  # Output: [0, 9, 8, 6, 8, 3]


# 5. Clear()
# clear() removes all elements from the list.

Number = [3,8,6,8,9,0]
Number.clear()
print(Number)  # Output: []


# 6. Copy()
# copy() returns a shallow copy of the list.

Number = [3,8,6,8,9,0]
copied_Number = Number.copy()
print(copied_Number)  # Output: [3, 8, 6, 8, 9, 0]

# Note that copy() creates a new reference to the same objects, so modifications to the copied list will affect the original list if it contains mutable objects.
