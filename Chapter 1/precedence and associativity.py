# precedence and associativity 

# precedence and associativity rules determine the order in which operators are evaluated when multiple operators are used in an expression.

# Precedence Rule:
# Precedence defines the priority of operators. Operators with higher precedence are evaluated first.

# Here's the precedence order in Python:

# 1. Parentheses '()'
# 2. Exponentiation '**'
# 3. Unary operators '+', '-', '~', 'not'
# 4. Multiplication '*', Division '/', Floor Division '//', Modulus '%'
# 5. Addition '+', Subtraction '-'
# 6. Comparison operators '==', '!=', '<', '>', '<=', '>=', 'is', 'is not'
# 7. Logical operators 'and', 'or', 'not'
# 8. Assignment operators '=', '+=', '-=', '*=', '/=', '//=', '%=', etc.


# Associativity Rule:
# Associativity defines the direction in which operators with the same precedence are evaluated.

# There are two types of associativity:

# 1. Left-to-Right (LTR) : Operators are evaluated from left to right.
# 2. Right-to-Left (RTL) : Operators are evaluated from right to left.

# Here's the associativity of operators in Python:
# 1. Most operators are LTR (e.g., '+', '-', '*', '/', etc.)
# 2. Exponentiation '**' is RTL
# 3. Assignment operators are RTL


# Example 1 :

print(2 + 3 * 4)

# Precedence: Multiplication ('*') has higher precedence than Addition ('+')

# Associativity: Addition ('+') is LTR

# First the highest value precedence will evaluate (3*4) and then his lower value precedence will evaluate 
# Evaluation: (2 + (3 * 4)) 
# = 2 + 12 
# = 14

# By following these rules, you can ensure that your Python expressions are evaluated correctly.