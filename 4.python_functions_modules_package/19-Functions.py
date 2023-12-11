# Python Functions
###########################################################################################
# A function is a block of code that performs a specific task.
# There are two types of functions:
# built-in functions
# user-defined functions

# 1. built-in function:
# These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:
# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

# -----------------------------------------------------------------------------------------

# 2. user-defined functions:
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.
# Syntax:
# def function_name(parameters):
#     Code and Statements
# Create a function using the def keyword, followed by a function name, followed by a parenthesis (()) and a colon(:).
# Any parameters and arguments should be placed within the parentheses.
# Rules to naming function are similar to that of naming variables.
# Any statements and other code within the function should be indented.

# Call a function:
# We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

# Example:
def name(fname, lname):
    print("Hello,", fname, lname)


name("Avi", "M")


###########################################################################################

# Python Function Declaration

# The syntax to declare a function is:

# def function_name(arguments):
# function body

#     return
# Here,
# def - keyword used to declare a function
# function_name - any name given to the function
# arguments - any value passed to function
# return (optional) - returns value from a function


# Ex:
def greet():
    print('Hello World!')


# call the function
greet()
print('Outside function')

# Here,
# When the function is called, the control of the program goes to the function definition.
# All codes inside the function are executed.
# The control of the program jumps to the next statement after the function call.

###########################################################################################

# Python Function Arguments

# As mentioned earlier, a function can also have arguments.
# An argument is a value that is accepted by a function. For example,

# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print('Sum: ',sum)


# function with no argument
def add_numbers():
     # code

# If we create a function with arguments, we need to pass the corresponding values while calling them. For example,

     # function call with two values
     add_numbers(5, 4)

     # function call with no value
     add_numbers()

# Here, add_numbers(5, 4) specifies that arguments num1 and num2 will get values 5 and 4 respectively.

# Example 1: Python Function Arguments
# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ",sum)

# function call with two values
add_numbers(5, 4)
# Output: Sum: 9

# In the above example, we have created a function named add_numbers() with arguments: num1 and num2.

# There are four types of arguments that we can provide in a function:
# Default Arguments
# Keyword Arguments
# Required Arguments
# Variable-length Arguments

# -----------------------------------------------------------------------------------------

# Default arguments:
# We can provide a default value while creating a function.
# This way the function assumes a default value even if a value is not provided in the function call for that argument.
# Example:
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")
# -----------------------------------------------------------------------------------------

# Keyword arguments:
# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name.
# Hence, the the order in which the arguments are passed does not matter.
# Example:
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")
# -----------------------------------------------------------------------------------------

# Required arguments:
# In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments
# in the correct positional order and the number of arguments passed should match with actual function definition.
# Example 1: when number of arguments passed does not match to the actual function definition.
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name('peter','ego','quill')
# name("Peter", "Quill") # error because we are not passing 3rd arg.

# -----------------------------------------------------------------------------------------

# Variable-length arguments:
# Sometimes we may need to pass more arguments than those defined in the actual function.
# This can be done using variable-length arguments.

# There are two ways to achieve this:
# Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function.
# The function accesses the arguments by processing them in the form of tuple.
# Example:
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")

# Keyword Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function.
# The function accesses the arguments by processing them in the form of a dictionary.
# Example:

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

###########################################################################################

# The return Statement in Python

# A Python function may or may not return a value.
# If we want our function to return some value to a function call, we use the return statement. For example,

# def add_numbers():
#     ...
#     return sum
# Here, we are returning the variable sum to the function call.

# Example 2: Function return Type
# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)
print('Square:',square)
# Output: Square: 9

# In the above example, we have created a function named find_square().
# The function accepts a number and returns the square of the number.

# Example 3: Add Two Numbers
# function that adds two numbers
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum
# calling function with two values
result = add_numbers(5, 4)
print('Sum: ', result)
# Output: Sum: 9

###########################################################################################

# Python Recursion
# We can let the function call itself, such a process is known as calling a function recursively in python.
# Example:
def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))

# Driver Code
num = 7;
print("number: ",num)
print("Factorial: ",factorial(num))

# Output:
# number:  7
# Factorial:  5040

###########################################################################################

# Python Lambda/Anonymous Function

# In Python, a lambda function is a special type of function without the function name. For example,
lambda: print('Hello World')
# Here, we have created a lambda function that prints 'Hello World'.

# Python lambda Function Declaration

# We use the lambda keyword instead of def to create a lambda function.
# Here's the syntax to declare the lambda function:
# lambda argument(s) : expression
# Here,
# argument(s) - any value passed to the lambda function
# expression - expression is executed and returned
# Let's see an example,

greet = lambda : print('Hello World')
# call the lambda
greet()

# Here, we have defined a lambda function and assigned it to the variable named greet.
# The lambda function above simply prints the text 'Hello World'.
# Note: This lambda function doesn't have any arguments.

# ex:
# declare a lambda function
greet = lambda : print('Hello World')
# call lambda function
greet()
# Output: Hello World

# In the above example, we have defined a lambda function and assigned it to the greet variable.
# When we call the lambda function, the print() statement inside the lambda function is executed.

# Ex: Python lambda Function with an Argument
# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)
# lambda call
greet_user('Avinash')

# In the above example, we have assigned a lambda function to the greet_user variable.
# Here, name after the lambda keyword specifies that the lambda function accepts the argument named name.
# Notice the call of lambda function,
# greet_user('Avinash')
# Here, we have passed a string value 'Avinash' to our lambda function.
# And finally, the statement inside the lambda function is executed.

###########################################################################################

# Now you will have better understanding of Global & local variables concept.

###########################################################################################

# Ex:
def largest_Num(a,b):
    if a>b:
        return a
    else:
        return b

num = largest_Num(5,10)
print("Largest Num: ",num)

num = largest_Num(12,10)
print("Largest Num: ",num)