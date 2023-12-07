# Python Variables
#https://www.codewithharry.com/tutorial/python-variables/
#https://www.programiz.com/python-programming/variables-constants-literals

###########################################################################################
#Python is dynamically typed programming lang.

# Variables are containers that store information that can be manipulated and
# referenced later by the programmer within the code.
# In python, the programmer does not need to declare the variable type explicitly;
# we just need to assign the value to the variable.
# Example:

name = "Avinash"   #type str
age = 20            #type int
passed = True       #type bool

# Printing multiple variables in single line.
print(name,age,passed)
###########################################################################################
# It is always advisable to keep variable names descriptive and
# to follow a set of conventions while creating variables:

# Variable name can only contain alphanumeric characters and underscores (A-z, 0-9, and _ )
# Variable name must start with a letter or the underscore character.
# Variables are case-sensitive.
# Variable name cannot start with a number.
# Example

Color = "yellow"    #valid variable name
cOlor = "red"       #valid variable name
_color = "blue"     #valid variable name
#5color = "green"   #invalid variable name
#$color = "orange"  #invalid variable name
###########################################################################################

# Sometimes, a multi-word variable name can be difficult to read by the reader.
# To make it more readable, the programmer can do the following:
# Example:

NameOfCity = "Mumbai"       #Pascal case
nameOfCity = "Berlin"       #Camel case
name_of_city = "Moscow"     #snake case
###########################################################################################
# Local Variable:
# A local variable is created within a function and can be only used inside that function.
# Such a variable has a local scope.

# Global Variable:
# A global variable is created in the main body of the code and can be used anywhere within the code.
# Such a variable has a global scope.
###########################################################################################

# Declaring Variable and Assigning Values
# Python doesn't tie us to pronounce a variable prior to involving it in the application.
# It permits us to make a variable at the necessary time.
# In Python, we don't have to explicitly declare variables.
# The variable is declared automatically whenever a value is added to it.
# The equal (=) operator is utilized to assign worth to a variable.

###########################################################################################

# Data Types & Variable Declaration

# int
a = 13
print('this is a: ',a)
print('datatype of a:', type(a)) # to know the datatype
# or we can use print(type(a))

# string
b = "this is string"
print('this is b: ',b)
print('datatype of a:', type(b))

# decimal
c = 12.22
b = "this is string"
print('this is c: ',c)
print('datatype of a:', type(c))

#print with + & ,
p = "Python "
q = "is "
r = "awesome"
print(p + q + r)
print(p,q,r)

###########################################################################################
# single line declaration
xyz = 3, 3.33, "three"
print('printing values of x,y,z: ',xyz)
# you cannot print them separately

x, y, z = "Orange", "Banana", "Cherry"
print('printing values of x: ',x)
print('printing values of y: ',y)
print('printing values of z: ',z)
###########################################################################################
#Changing the Value of a Variable in Python
site_name = 'programiz.pro'
print('this is site name: ',site_name)
###########################################################################################
# assigning a new value to site_name
site_name = 'apple.com'
print('this is site name after new value: ',site_name)
###########################################################################################
#If we want to assign the same value to multiple variables at once, we can do this as:

site1 = site2 = 'programiz.com'
print('this is site1: ',site1) # prints programiz.com
print('this is site2: ',site2) # prints programiz.com
###########################################################################################

n = 50
m = 55
print("this is n: ",n)
print("this is m: ",m)
print("this is n: ",n," this is m: ",m)

###########################################################################################

i=1
j=2
print(i,j) #1,2

# Swapping Values
i,j = j, i
# in the above statement, the vale of 'i' is assigned to 'j' and vale of 'j' is assigned to 'i'
print(i,j) #2,1

###########################################################################################

# Variables can be used in operations like actual values. Such as
# Using variables in operations
x = 5
y = 3
sum = x + y
print(sum)

###########################################################################################
# Reassigning Variables: Variable values can be changed. New values can be the same or
# different types. Such as
# Reassigning variables
x = 5
print("this is x before: ",x)
x = x + 1 # x is now 6
print("this is x after: ",x)

name = "Alice"
print("this is Name before: ",name)
name = "Bob" # name is now "Bob"
print("this is Name after: ",name)

###########################################################################################
# Dynamic Typing
# Python is dynamically typed, thus variables can hold values of different kinds and change
# type during execution. Know this:
# Dynamic Typing: Python doesn't require variable types before assigning values. Runtime
# type inference is based on variable value. You can use different data types without specifying
# them.
# Dynamic typing lets you freely assign values of multiple kinds to variables. Such as
# Dynamic typing example
age = 25 # age is an integer
age = "John" # age is now a string
age = 3.14 # age is now a float
###########################################################################################
# Python variable type changes dynamically. Python will change a variable's type when you
# reassign a value. Such as
# Changing variable type
x = 5 # x is an integer
x = "Hello" # x is now a string
x = [1, 2, 3] # x is now a list

###########################################################################################
# Dynamic Typing benefits:
# Flexibility: Working with different data types without declaring the type makes
# Python code more concise and expressive.
# Dynamic typing makes variable assignments and reassignments easier, letting you
# focus on code logic rather than type definitions.
# Dynamic typing lets you easily experiment and prototype concepts by changing variable types.
# Dynamic type allows versatility, but there are risks:
# Type Errors: Since variable types can change dynamically, operations or methods
# incompatible with the current variable type might cause type errors.
# Readability: Dynamic typing permits expressive code, but variable names must
# appropriately reflect their purpose and content to maintain readability.

###########################################################################################
# deleting variable using 'del' keyword

num1 = 10
num2 = 20
print('Value of num1 before delete: ', num1)
print('Value of num2 before delete: ', num2)

#deleting num1 value

del num1
print('Value of num1 after delete: ', num1)
# we get NameError: name 'num1' is not defined.
###########################################################################################