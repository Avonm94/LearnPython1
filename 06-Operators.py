# Python operators
###########################################################################################
# Operators are special symbols that perform operations on variables and values.
# Types of Operators:
    # Arithmetic operators
    # Comparison operators
    # Assignment Operators
    # Logical Operators
    # Bitwise Operators
    # Membership Operators
    # Identity Operators
###########################################################################################

# Arithmetic operators

# + (Addition) -->	It is used to add two operands. For example, if a = 10, b = 10 => a+b = 20

# - (Subtraction) --> It is used to subtract the second operand from the first operand.
#  If the first operand is less than the second operand, the value results negative.
#  For example, if a = 20, b = 5 => a - b = 15.

# / (divide) --> It returns the quotient after dividing the first operand by the second operand.
#  For example, if a = 20, b = 10 => a/b = 2.0

# * (Multiplication) --> It is used to multiply one operand with the other.
#  For example, if a = 20, b = 4 => a * b = 80

# % (reminder) --> It returns the reminder after dividing the first operand by the second operand.
#  For example, if a = 20, b = 10 => a%b = 0

# ** (Exponent) -->	As it calculates the first operand's power to the second operand, it is an exponent operator.

# // (Floor division) --> It provides the quotient's floor value, which is obtained by dividing the two operands.

# Example 1:
a = 32    # Initialize the value of a
b = 6      # Initialize the value of b
print('Addition of two numbers:',a+b)
print('Subtraction of two numbers:',a-b)
print('Multiplication of two numbers:',a*b)
print('Division of two numbers:',a/b)
print('Reminder of two numbers:',a%b)
print('Exponent of two numbers:',a**b)
print('Floor division of two numbers:',a//b)

# Example 2
a = 7
b = 2

# addition
print ('Sum: ', a + b)
# subtraction
print ('Subtraction: ', a - b)
# multiplication
print ('Multiplication: ', a * b)
# division
print ('Division: ', a / b)
# floor division
print ('Floor Division: ', a // b)
# modulo
print ('Modulo: ', a % b)
# a to the power b
print ('Power: ', a ** b)

###########################################################################################

# Comparison operators:
# Comparison operators mainly use it for comparison.Comparison operators compare the values of the two operands
# and return a true or false Boolean value in accordance.

# == : If the value of two operands is equal, then the condition becomes true.
# != : If the value of two operands is not equal, then the condition becomes true.
# <= : The condition is met if the first operand is smaller than or equal to the second operand.
# >= : The condition is met if the first operand is greater than or equal to the second operand.
# >  : If the first operand is greater than the second operand, then the condition becomes true.
# <  : If the first operand is less than the second operand, then the condition becomes true.

# Example 1:
a = 32      # Initialize the value of a
b = 6       # Initialize the value of b
print('Two numbers are equal or not:',a==b)
print('Two numbers are not equal or not:',a!=b)
print('a is less than or equal to b:',a<=b)
print('a is greater than or equal to b:',a>=b)
print('a is greater b:',a>b)
print('a is less than b:',a<b)

# Example 2
a = 5
b = 2
# equal to operator
print('a == b =', a == b)
# not equal to operator
print('a != b =', a != b)
# greater than operator
print('a > b =', a > b)
# less than operator
print('a < b =', a < b)
# greater than or equal to operator
print('a >= b =', a >= b)
# less than or equal to operator
print('a <= b =', a <= b)

###########################################################################################

# Assignment Operators
# Using the assignment operators, the right expression's value is assigned to the left operand.

# =	It assigns the value of the right expression to the left operand.

# +=	By multiplying the value of the right operand by the value of the left operand,
# the left operand receives a changed value.
# For example, if a = 10, b = 20 => a+ = b will be equal to a = a+ b and therefore, a = 30.

# -=	It decreases the value of the left operand by the value of the right operand
# and assigns the modified value back to left operand.
# For example, if a = 20, b = 10 => a- = b will be equal to a = a- b and therefore, a = 10.

# *=	It multiplies the value of the left operand by the value of the right operand
# and assigns the modified value back to then the left operand.
# For example, if a = 10, b = 20 => a* = b will be equal to a = a* b and therefore, a = 200.

# %=	It divides the value of the left operand by the value of the right operand
# and assigns the reminder back to the left operand.
# For example, if a = 20, b = 10 => a % = b will be equal to a = a % b and therefore, a = 0.

# **=	a**=b will be equal to a=a**b, for example, if a = 4, b =2, a**=b will assign 4**2 = 16 to a.

# //=	A//=b will be equal to a = a// b, for example, if a = 4, b = 3, a//=b will assign 4//3 = 1 to a.

# Example 1
a = 32         # Initialize the value of a
b = 6          # Initialize the value of b
print('a=b:', a==b)
print('a+=b:', a+b)
print('a-=b:', a-b)
print('a*=b:', a*b)
print('a%=b:', a%b)
print('a**=b:', a**b)
print('a//=b:', a//b)

# Example 2
# assign 10 to a
a = 10
# assign 5 to b
b = 5
# assign the sum of a and b to a
a += b      # a = a + b
print(a)
# Output: 15

###########################################################################################

# Logical Operators:
# Logical operators are used to combine conditional statements:

# and = Returns True if both statements are true	x < 5 and  x < 10
# or = Returns True if one of the statements is true	x < 5 or x < 4
# not = Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

# Example 1
a = 5          # initialize the value of a
print('Is this statement true?:',a > 3 and a < 5)
print('Any one statement is true?:',a > 3 or a < 5)
print('Each statement is true then return False and vice-versa:',(not(a > 3 and a < 5)))

# Example 2
# logical AND
print(True and True)     # True
print(True and False)    # False
# logical OR
print(True or False)     # True
# logical NOT
print(not True)          # False

###########################################################################################

# Bitwise Operator
# Bitwise operators are used to deal with binary operations.

# & (binary and)	A 1 is copied to the result if both bits in two operands at the same location are 1.
# If not, 0 is copied.

# | (binary or)	The resulting bit will be 0 if both the bits are zero; otherwise,
# the resulting bit will be 1.

# ^ (binary xor)	If the two bits are different, the outcome bit will be 1, else it will be 0.

# ~ (negation)	The operand's bits are calculated as their negations,
# so if one bit is 0, the next bit will be 1, and vice versa.

# << (left shift)	The number of bits in the right operand is multiplied by the leftward shift
# of the value of the left operand.

# >> (right shift)	The left operand is moved right by the number of bits present in the right operand.

# Bitwise operators act on operands as if they were strings of binary digits.
# They operate bit by bit, hence the name.
# For example, 2 is 10 in binary and 7 is 111.
# In the table below:
# Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)

# Operator --> Meaning --> Example
# & --> Bitwise AND --> x & y = 0 (0000 0000)
# | --> Bitwise OR --> x | y = 14 (0000 1110)
# ~ --> Bitwise NOT --> ~x = -11 (1111 0101)
# ^ --> Bitwise XOR  --> x ^ y = 14 (0000 1110)
# >> --> Bitwise right shift --> x >> 2 = 2 (0000 0010)
# << --> Bitwise left shift --> x << 2 = 40 (0010 1000)

# Example
x = 10        # initialize the value of x
y = 4         # initialize the value of y
print('x&y:', x&y)
print('x|y:', x|y)
print('x^y:', x^y)
print('~x:', ~x)
print('x<<2:', x<<2)
print('x>>2:', x>>2)

###########################################################################################
# Special Operators:

# Membership Operators:
# The membership of a value inside a Python data structure can be verified using Python membership operators.
# The result is true if the value is in the data structure; otherwise, it returns false.

# in = If the first operand cannot be found in the second operand,
# it is evaluated to be true (list, tuple, or dictionary).
# True if value/variable is found in the sequence

# not in = If the first operand is not present in the second operand,
# the evaluation is true (list, tuple, or dictionary).
# True if value/variable is not found in the sequence

# Example:
x = 'Hello world'
y = {1:'a', 2:'b'}

# check if 'H' is present in x string
print('H' in x)  # prints True

# check if 'hello' is present in x string
print('hello' not in x)  # prints True

# check if '1' key is present in y
print(1 in y)  # prints True

# check if 'a' key is present in y
print('a' in y)  # prints False

# Example 2:
x = ["Rose", "Lotus"]
print(' Is value Present?', "Rose" in x)
print(' Is value not Present?', "Riya" not in x)

###########################################################################################

# Identity operators:
# In Python, is and is not are used to check if two values are located on the same part of the memory.
# Two variables that are equal does not imply that they are identical.

# is = True if the operands are identical (refer to the same object) x is True

# is not = True if the operands are not identical (do not refer to the same object)	x is not True

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1)  # prints False
print(x2 is y2)  # prints True
print(x3 is y3)  # prints False

# Example 2
a = ["Rose", "Lotus"]
b = ["Rose", "Lotus"]
c = a
print(a is c)
print(a is not c)
print(a is b)
print(a is not b)
print(a == b)
print(a != b)

###########################################################################################

# Operator Precedence
# The order in which the operators are examined is crucial to understand since
# it tells us which operator needs to be considered first.
# Below is a list of the Python operators' precedence tables.

# Operator --> Description
# ** --> Overall other operators employed in the expression, the exponent operator is given precedence.
# ~ + - --> the minus, unary plus, and negation.
# * / % // --> the division of the floor, the modules, the division, and the multiplication.
# + - --> Binary plus, and minus
# >> << --> Left shift. and right shift
# & --> Binary and.
# ^ | --> Binary xor, and or
# <= < > >= --> Comparison operators (less than, less than equal to, greater than, greater then equal to).
# <> == != --> Equality operators.
# = %= /= //= -= += *= **= --> Assignment operators
# is is not --> Identity operators
# in not in --> Membership operators
# not or and --> Logical operators

###########################################################################################

# Operator Precedence in Python:
# Parenthesis ()
# Exponential **
# Complement, unary plus, unary minus ~ , +,  -
# Multiply, divide, modulus, floor division *,  /,  %,  //
# Addition, subtraction +, -
# Left shift and right shift operators <<, >>
# Bitwise and &
# Bitwise or and xor ^, |
# Comparison operators <, >, >=, <=
# Equality operators ==, !=
# Assignment operators=, %=, /=, //=, -=, +=, *= , **=
# Identity operators is, is not
# Membership operators in, not in
# Logical operators and, or, not
