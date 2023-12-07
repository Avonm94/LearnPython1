# Python has a set of keywords that are reserved words that
# cannot be used as variable names, function names, or any other identifiers:

# Keyword: Description
###########################################################################################
# and: A logical operator
# as: To create an alias
# assert: For debugging
# break: To break out of a loop
# class: To define a class
# continue: To continue to the next iteration of a loop
# def: To define a function
# del: To delete an object
# elif: Used in conditional 3.statements, same as else if
# else: Used in conditional 3.statements
# except: Used with exceptions, what to do when an exception occurs
# False: Boolean value, result of comparison operations
# finally: Used with exceptions, a block of code that will be executed no matter if there is an exception or not
# for: To create a for loop
# from: To import specific parts of a module
# global: To declare a global variable
# if: To make a conditional statement
# import: To import a module
# in: To check if a value is present in a list, tuple, etc.
# is: To test if two variables are equal
# lambda: To create an anonymous function
# None: Represents a null value
# nonlocal: To declare a non-local variable
# not: A logical operator
# or: A logical operator
# pass: A null statement, a statement that will do nothing
# raise: To raise an exception
# return: To exit a function and return a value
# True: Boolean value, result of comparison operations
# try: To make a try...except statement
# while: To create a while loop
# with: Used to simplify exception handling
# yield: To end a function, returns a generator
###########################################################################################

# importing a keyword library which has lists
import keyword

# displaying the complete list using "kwlist()."
print("The set of keywords in this version is: ")
print(keyword.kwlist)

# By calling help(), you can retrieve a list of currently offered keywords:
help("keywords")

###########################################################################################
