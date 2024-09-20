# step argument in range function 

# step argument in range() function specifies the increment between consecutive values.

# Syntax: range(start, stop, step)

# Arguments:
# 1. start: Initial value (inclusive)
# 2. stop: Final value (exclusive)
# 3. step: Increment between values


# Positive Step

for i in range(1, 10, 2):
    print(i)


# Negative Step

for i in range(10, 1, -2):
    print(i)


# Default Step

for i in range(5):
    print(i)


# Key Points:
# 1. step can be positive or negative.
# 2. step cannot be zero.
# 3. Omitting step defaults to 1.


# Usage:
# 1. Generate sequences with custom increments.
# 2. Iterate over ranges in reverse order.
# 3. Create lists with specific intervals.


# Examples:

# Generate even numbers
evens = list(range(0, 20, 2))
print(evens)

# Generate odd numbers
odds = list(range(1, 20, 2))
print(odds)

# Iterate over range in reverse
for i in range(10, 0, -1):
    print(i)
