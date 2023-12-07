# Print Statement and Comments
# https://www.codewithharry.com/tutorial/python-comments/
###########################################################################################

# Syntax of print()
# print(object= separator= end= file= flush=)
# To print we use the keyword 'print'
print("Hello World")

# In the above code, the print() function is taking a single parameter.

# However, the actual syntax of the print function accepts 5 parameters
# object - value(s) to be printed
# sep (optional) - allows us to separate multiple objects inside print().
# end (optional) - allows us to add specific values like new line "\n", tab "\t"
# file (optional) - where the values are printed. It's default value is sys.stdout (screen)
# flush (optional) - boolean specifying if the output is flushed or buffered. Default: False

# Example 1: Python Print Statement
print('Good Morning!')
print('It is rainy today')
# Good Morning!
# It is rainy today

# In the above example, the print() statement only includes the object to be printed.
# Here, the value for end is not used. Hence, it takes the default value '\n'.

# So we get the output in two different lines.

# Example 2: Python print() with end Parameter
# print with end whitespace
print('Good Morning!', end= ' ')
print('It is rainy today')
# Good Morning! It is rainy today

# Example 3: Python print() with sep parameter
print('New Year', 2023, 'See you soon!', sep= '. ')
# New Year. 2023. See you soon!

###########################################################################################

# This is a Single-Line Comment using '#'
print("Hellow World.")  # Printing Hello World

print("Python Program")
# print("Python Program")

# To write multi-line comments, you can use ‘#’ at each line, or you can use the multiline string.
# Printing "A, B, C, D"
print("A,B,C,D")

"""This is multiline comments
Using 3 double quotes."""

'''This is multiline comments
Using 3 single quotes.'''

###########################################################################################
# Line Continuation:
# To write a code in multiline without confusing the python interpreter,
# is by using a backslash \ at the end of each line to explicitly denote line continuation.
# For example,

sum = 123 + \
      456 + \
      789
print(sum)  # this will print sum of 123,456,789

###########################################################################################

# Expressions enclosed in ( ), [ ] or { } brackets don't need a backward slash for line continuation.
# For example,

vowels = ['a', 'e', 'i',
          'o', 'u']
print(vowels)

# Blank lines in between a program are ignored by python.

# In one line only a single executable statement should be written
# and the line change act as command terminator in python.
# To write two separate executable 3.statements in a single line,
# you should use a semicolon; to separate the commands. For example,

print("Hello, World!")
print("This is second line")

###########################################################################################


