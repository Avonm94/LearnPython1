# Python 3.statements: Flow Control Statements

# 1.Conditional Statement --> if, if..else, elif (if...elif...else), Nested if.
# 2.Looping Statement --> for, while.
# 3.Jumping Statement --> Break, continue.

# Indentation
# Python relies on indentation (whitespace at the beginning of a line)
# to define scope in the code. Other programming languages often use curly-brackets for this purpose.

###########################################################################################

# 1.Conditional Statement
# Python Conditions: python supports the usual logical conditions from mathematics:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# ----------------------------------------------------------------------------------------

# 1. if statement:

# The if statement evaluates the condition.
# If the condition is evaluated to True, the code inside the body of if is executed.
# If the condition is evaluated to False, the code inside the body of if is skipped.
# The syntax of if statement in Python is-
# if condition:
#    body of an if statement
# semicolon after condition is part of syntax.

# Ex1: Check if the number is greater than 0
number1 = 10
if number1 > 0:  # the condition is true
    print('Number is positive.')  # if block will be executed.
print('outer statement after condition is true')

number2 = -5
if number2 > 0:  # the condition is false
    print('Number is positive.')  # if block will be skipped.
print('outer statement after condition is false')

# Ex2:
applePrice = 180
budget = 200
if applePrice <= budget:  # the condition is true
    print("Alexa, add 1kg Apples to the cart.")  # if block will be executed.

# Ex3:
a = 33
b = 200
if b > a:
    print("b is greater than a")

# ----------------------------------------------------------------------------------------

# 2. Python if...else Statement:

# An if a statement can have an optional else clause.

# The if...else statement evaluates the given condition:

# If the condition evaluates to True,
    # the code inside if is executed
    # the code inside else is skipped

# If the condition evaluates to False,
    # the code inside else is executed
    # the code inside if is skipped

# The syntax of if...else a statement is:
# if condition:
      # block of code if condition is True
# else:
      # block of code if condition is False

# Ex1:
number1 = 10
if number1 > 0: # True
    print('Positive number')
else:
    print('Negative number')
print('This statement is always executed')

number2 = 10
if number2 > 0: # False
    print('Positive number')
else:
    print('Negative number')
print('This statement is always executed')

# Ex2:
x = 10
y = 5
if x > y: # True
    print("x is greater than y")
else:
    print("y is greater than or equal to x")

# Ex3:
applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

# ----------------------------------------------------------------------------------------

# 3. Python if...elif...else Statement

# The if...else statement is used to execute a block of code among two alternatives.
# However, if we need to make a choice between more than two alternatives,
# then we use the if...elif...else statement.
# The syntax of the if...elif...else statement is:

# if condition1:
#     # code block 1
# elif condition2:
#     # code block 2
# else:
#     # code block 3

# Here,
# If condition1 evaluates to true, code block 1 is executed.
# If condition1 evaluates to false, then condition2 is evaluated.
# If condition2 is true, code block 2 is executed.
# If condition2 is false, code block 3 is executed.

# Ex1:
number1 = 0
if number1 > 0: # true
    print(number1,"- Positive number")
elif number1 == 0: # True
    print(number1,'- Zero')
else:
    print(number1,'- Negative number')
print('This statement is always executed')


number2 = 8
if number2 > 0: # true
    print(number2,"- Positive number")
elif number2 == 0:
    print(number2,'- Zero')
else:
    print(number2,'- Negative number')
print('This statement is always executed')


number3 = -3
if number3 > 0: #false
    print(number3,"- Positive number")
elif number3 == 0:
    print(number3,'- Zero')
else:
    print(number3,'- Negative number')
print('This statement is always executed')

# In the above example, we have created a variable named number with the value 0.
# Here, we have two condition expressions:
# Here, both the conditions evaluate to False. Hence the statement inside the body of else is executed.

# Ex2:
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# In this example a is equal to b, so the first condition is not true,
# but the elif condition is true, so we print to screen that "a and b are equal".

# Ex3:
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# In this example a is greater than b, so the first condition is not true,
# also the elif condition is not true, so we go to the else condition
# and print to screen that "a is greater than b".

# ----------------------------------------------------------------------------------------

# 4.Python Nested if 3.statements

# We can also use an if statement inside of an if statement. This is known as a nested if statement.
# The syntax of nested if statement is:
# outer if statement
# if condition1:
#     # statement(s)
#
#     # inner if statement
#     if condition2:
#         # statement(s)
# Notes:
# We can add else and elif 3.statements to the inner if statement as required.
# We can also insert inner if statement inside the outer else or elif 3.statements(if they exist)
# We can nest multiple layers of if 3.statements.

# Ex:
number = 5
if (number >= 0): # outer if statement
    if number == 0:  # inner if statement
        print('Number is 0')
    else: # inner else statement
        print('Number is positive')
else: # outer else statement
    print('Number is negative')

#In the above example, we have used a nested if statement to check whether
# the given number is positive, negative, or 0.

# Ex2:
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Ex3
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

###########################################################################################

# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.
# Example: One line if statement:
if a > b: print("a is greater than b")

# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
# Example: One line if else statement:
a = 2
b = 330
print("A") if a > b else print("B")

# Example One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# This technique is known as Ternary Operators, or Conditional Expressions.

# ----------------------------------------------------------------------------------------

# And: The and keyword is a logical operator, and is used to combine conditional 3.statements:
# Example: Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# ----------------------------------------------------------------------------------------

# Or: The or keyword is a logical operator, and is used to combine conditional 3.statements:
# Example: Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# ----------------------------------------------------------------------------------------

# Not: The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
# Example: Test if a is NOT greater than b:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

###########################################################################################
# ----------------------------------------------------------------------------------------

# The pass Statement
# if 3.statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.
# Example
a = 33
b = 200
if b > a:
  pass

###########################################################################################