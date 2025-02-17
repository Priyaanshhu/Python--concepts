# break and continue statement 

# 'break' and 'continue' are control flow statements used to manipulate the flow of loops

# Break Statement: Exits the loop immediately

for i in range(11):
    if i == 5:
        break
    print(i)

# Continue Statement: Skips to the next iteration.

for i in range(11):
    if i == 5:
        continue
    print(i)


# Usage:
# break:
#     - Exit loop when a condition is met.
#     - Avoid unnecessary iterations.
# continue:
#     - Skip specific iterations.
#     - Filter out unwanted values.
