# Python break and continue
###########################################################################################

# Python break Statement
# The break statement is used to terminate the loop immediately when it is encountered.
# The break statement is almost always used with decision-making statements.

# Python break Statement with for Loop
# We can use the break statement with the for loop to terminate the loop when a certain condition is met. For example,

for i in range(5):
    if i == 3:
        break
    print(i)

# In the above example, we have used the for loop to print the value of i.
# Notice the use of the break statement,
# if i == 3:
#     break
# Here, when i is equal to 3, the break statement terminates the loop.
# Hence, the output doesn't include values after 2.

# -----------------------------------------------------------------------------------------

# Python break Statement with while Loop
# We can also terminate the while loop using the break statement. For example,

# program to find first 5 multiples of 6
i = 1
while i <= 10:
    print('6 * ',(i), '=',6 * i)

    if i >= 5:
        break
    i = i + 1
# In the above example, we have used the while loop to find the first 5 multiples of 6. Here notice the line,
# if i >= 5:
#     break
# This means when i is greater than or equal to 5, the while loop is terminated.

# Ex:
i = 1
while (i <= 10):
    i = i + 1
    if (i == 5):
        break
    print(i)

# Ex:
for i in range(1, 10):
    print(i)
    if (i == 5):
        break

###########################################################################################

# Python continue Statement
# The continue statement is used to skip the current iteration of the loop and
# the control flow of the program goes to the next iteration.

# Python continue Statement with for Loop
# We can use the continue statement with the for loop to skip the current iteration of the loop.
# Then the control of the program jumps to the next iteration. For example,

for i in range(5):
    if i == 3:
        continue
    print(i)

# In the above example, we have used the for loop to print the value of i. Notice the use of the continue statement,
# if i == 3:
#     continue
# Here, when i is equal to 3, the continue statement is executed.
# Hence, the value 3 is not printed to the output.

# -----------------------------------------------------------------------------------------

# Python continue Statement with while Loop
# In Python, we can also skip the current iteration of the while loop using the continue statement. For example,

# program to print odd numbers from 1 to 10
num = 0
while num < 10:
    num += 1
    if (num % 2) == 0:
        continue
    print(num)

# In the above example, we have used the while loop to print the odd numbers between 1 to 10. Notice the line,
# if (num % 2) == 0:
#     continue
# Here, when the number is even, the continue statement skips the current iteration and starts the next iteration.

# Ex:
for i in range(1,10):
    if(i%2 == 0):
        continue
    print(i)

# Ex:
i = 1
while (i <= 10):
    i = i + 1
    if (i%2 != 0):
        continue
    print(i)

###########################################################################################

# Python pass Statement

# In Python programming, the pass statement is a null statement which can be used as a placeholder for future code.
# Suppose we have a loop or a function that is not implemented yet,
# but we want to implement it in the future. In such cases, we can use the pass statement.

# Using pass With Conditional Statement
n = 10
# use pass inside if statement
if n > 10:
    pass
print('Hello')

# Here, notice that we have used the pass statement inside the if statement.
# However, nothing happens when the pass is executed. It results in no operation (NOP).
# Suppose we didn't use pass or just put a comment as:
# n = 10
# if n > 10:
#     # write code later
# print('Hello')
# Here, we will get an error message: IndentationError: expected an indented block

# Note: The difference between a comment and a pass statement in Python is that
# while the interpreter ignores a comment entirely, pass is not ignored.

###########################################################################################
