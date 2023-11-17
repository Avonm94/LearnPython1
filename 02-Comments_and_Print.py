# Print Statement and Comments
# https://www.codewithharry.com/tutorial/python-comments/
###########################################################################################

# To print we use keyword 'print'
print("Hello World")

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
# To write two separate executable statements in a single line,
# you should use a semicolon; to separate the commands. For example,

print("Hello, World!");
print("This is second line")

###########################################################################################
