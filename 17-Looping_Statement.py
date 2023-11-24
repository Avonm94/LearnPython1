# Python Loops
###########################################################################################
# Python has two primitive loop commands:
# for loops
# while loops

# ----------------------------------------------------------------------------------------

# for loop:

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# The syntax of a for loop is:
# for val in sequence:
# statement(s)

# Here, val accesses each item of sequence on each iteration.
# The loop continues until we reach the last item in the sequence.

# Ex1:iterating over a string:
name = 'Avinash'
for i in name:
    print(i, end=", ")

# Ex2:iterating over a list
languages = ['Swift', 'Python', 'Go', 'JavaScript']
# run a loop for each item of the list
for language in languages:
    print(language)

# Ex3:iterating over a tuple:
colors = ("Red", "Green", "Blue", "Yellow")
for x in colors:
    print(x)

# ----------------------------------------------------------------------------------------

# For Loop with Python range()

# A range is a series of values between two numeric intervals.
# We use Python's built-in function range() to define a range of values.
# The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and ends at a specified number.

# For example,
values = range(4)
# Here, 4 inside range() defines a range containing values 0, 1, 2, 3.
# In Python, we can use for loop to iterate over a range.

# Ex:use of range() to define a range of values
values = range(4)
# iterate from i = 0 to i = 3
for i in values:
    print(i)

# In the above example, we have used the for loop to iterate over a range from 0 to 3.
# The value of i is set to 0, and it is updated to the next number
# of the range on each iteration. This process continues until 3 is reached.

# EX:specific range.
for k in range(4, 9):
    print(k)

# ----------------------------------------------------------------------------------------

# Python for loop with else
# A for loop can have an optional else block.
# The else part is executed when the loop is exhausted
# (after the loop iterates through every item of a sequence).
# Note: The else block will NOT be executed if the loop is stopped by a break statement.

# EX
digits = [0, 1, 5]
for i in digits:
    print(i)
else:
    print("No items left.")

# EX
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

# ----------------------------------------------------------------------------------------

# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
# Example: Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
    print("end of inner loop")
print("end of outerloop")

###########################################################################################

# while loop:

# Python while loop is used to run a block code until a certain condition is true.
# As soon as the condition becomes False, the interpreter comes out of the while
# The syntax of while loop is:
# while condition:
# body of while loop

# A while loop evaluates the condition
# If the condition evaluates to True, the code inside the while loop is executed.
# the condition is evaluated again.
# This process continues until the condition is False.
# When the condition evaluates to False, the loop stops.

# Ex1: # program to display numbers from 1 to 5
# initialize the variable
i = 1
n = 5
# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1

# Ex2:
count = 5
while (count > 0):
    print(count)
    count = count - 1

# Here, the count variable is set to 5 which decrements after each iteration.
# Depending upon the while loop condition, we need to either increment or decrement
# the counter variable (the variable count, in our case) or the loop will continue forever.

# Ex3: with else
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')

# Ex4: with else
counter = 0
while counter < 3:
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')

# Ex5: The else block will not execute if the while loop is terminated by a break statement.
counter = 0
while counter < 3:
    # loop ends because of break
    # the else part is not executed
    if counter == 1:
        break
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')

###########################################################################################

# Python for Vs while loops
# The for loop is usually used when the number of iterations is known. For example,

# this loop is iterated 4 times (0 to 3)
for i in range(4):
    print(i)

# The while loop is usually used when the number of iterations is unknown. For example,
# while condition:
# run code until the condition evaluates to False

###########################################################################################

# Nested Loops
# We can use loops inside other loops, such types of loops are called as nested loops.

# Example: nesting for loop in while loop
while (i <= 3):
    for k in range(1, 4):
        print(i, "*", k, "=", (i * k))
    i = i + 1
    print()

# Example: nesting while loop in for loop

for i in range(1, 4):
    k = 1
    while (k <= 3):
        print(i, "*", k, "=", (i * k))
        k = k + 1
    print()

###########################################################################################

# range():
# The range() function returns a sequence of numbers between the give range.
# range() returns an immutable sequence of numbers that can be easily converted to lists,
# tuples, sets etc.# Syntax of range()
# The range() function can take a maximum of three arguments:
# range(start, stop, step)
# The start and step parameters in range() are optional.

# Example: create a sequence of numbers from 0 to 3
numbers = range(4)
# iterating through the sequence of numbers
for i in numbers:
    print(i)

# Now, let's see how range() works with different number of arguments.

# numbers from 0 to 3 (4 is not included)
numbers = range(4)
print(list(numbers))  # [0, 1, 2, 3]
# if 0 or negative numbers are passed, we get an empty sequence
numbers = range(-4)
print(list(numbers))  # []

###########################################################################################

# Ex: Prin 0 to 10 incrementing order

i = 0
while i <= 10:
    print(i)
    i = i + 1

for x in range(11):
    print(x)

for x in range(1, 11):
    print(x)

# Ex: print only even-numbers 0 to 20

for i in range(0, 21, 2):  # incremented by 2
    print(i)

# Ex: Prin 0 to 10 decrementing order

j = 10
while j >= 0:
    print(j)
    j = j - 1

for x in range(10, 0, -1):
    print(x, end=",")

###########################################################################################
