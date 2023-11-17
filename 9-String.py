# Python String Data type
###########################################################################################
# Strings
# a string is a sequence of characters.
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'Hello' is the same as "Hello".

print("Hello")
print('Hello')

# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)

# Sometimes, the user might need to put quotation marks in between the strings.
# Example, consider the sentence: He said, “I want to eat an apple”.

print('He said, "I want to eat an apple".')
# OR
print("He said, \"I want to eat an apple\".")

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes or single quotes:

a = """I am learning python.
python is easy to learn."""
print(a)

a = '''I am Avinash.
I am learning python'''
print(a)

receipe = """
1. Heat the pan and add oil
2. Crack the egg
3. Add salt in egg and mix well
4. Pour the mixture in pan
5. Fry on medium heat
"""
print(receipe)

note = '''
This is a multiline string
It is used to display multiline message in the program
'''
print(note)

###########################################################################################
# Python String - operations

# Strings are Arrays
# strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type; a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
# Get the character at position 1 (remember that the first character has the position or index 0):

# Indexing:
a = "Hello, World!"
print(a[0])  # output = H
print(a[1])  # output = e
print(a[2])  # output = l
print(a[3])  # output = l
print(a[4])  # output = 0
print(a[0], a[1], a[2], a[3], a[4])

# Negative Indexing:
a = "Hello, World!"
print(a[-6])  # output = W
print(a[-5])  # output = o
print(a[-4])  # output = r
print(a[-3])  # output = l
print(a[-2])  # output = d
print(a[-1])  # output = !
print(a[-6], a[-5], a[-4], a[-3], a[-2], a[-1])

pie = "ApplePie"
print(pie[:5])
print(pie[6])  # returns character at specified index
print(pie[5:8])

# Slicing
# Access a range of characters in a string by using the slicing operator colon:
# Example:

pie = "ApplePie"
print(pie[:5])  # Slicing from Start
print(pie[5:])  # Slicing till End
print(pie[2:6])  # Slicing in between
print(pie[-8:])  # Slicing using negative index

str1 = 'hello Avinash'  # string str1
str2 = 'how are you'  # string str2
print(str1[0:2])  # printing the first two characters using slice operator
print(str1[4])  # printing 4th character of the string
print(str1 * 2)  # printing the string twice
print(str1 + str2)  # printing the concatenation of str1 and str2

# Slice From the Start
# By leaving out the start index, the range will start at the first character:
# Example
# Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

# Slice To the End
# By leaving out the end index, the range will go to the end:
# Example
# Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])

# Use negative indexes to start the slice from the end of the string:
# Example
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])

###########################################################################################

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Example
# Loop through the letters in the word "banana":

for x in "Hello":
    print(x)

alphabets = "ABCDE"
for i in alphabets:
    print(i)

###########################################################################################

# String Length
# To get the length of a string, use the len() function.
# Example
# The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))

fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

###########################################################################################

# Check String

# To check if a certain phrase or character is present in a string, we can use the keyword in.
# Example
# Check if "free" is present in the following text:
txt = "I love python !"
print("love" in txt)

# Use it in an if statement:
# Example
# Print only if "love" is present:
txt = "I love python !"
if "love" in txt:
    print("Yes, 'love' is present, in txt.'")

# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
# Example
# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

# Use it in an if statement:
# Example
# print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

###########################################################################################

# Python String - Modification
# Python has a set of built-in methods that you can use on strings.

str1 = "AbcDEfghIJ"
str2 = " Avinash !!!"
str3 = "i love python."
str4 = "Abcd1234"
str5 = "1234"

# upper() --> converts the string to uppercase.
print(str1.upper())

# lower() --> converts the string to lowercase.
print(str1.lower())

# capitalize() --> coverts only the first character of the string to uppercase
# and the rest other characters of the string are turned to lowercase.
# The string has no effect if the first character is already uppercase.
print(str3.capitalize())

# title() --> capitalizes each letter of the word within the string.
print(str3.title())

# strip() --> removes any space before and after the string.
print(str2.strip())

# rstrip() --> removes any trailing characters.
print(str2.rstrip("!"))

# replace() --> replaces substring inside
print(str3.replace("python", "java"))

# partition() --> returns a tuple

# find() --> returns the index of first occurrence of substring
print(str3.find("love"))

# split() --> splits string from left
print(str3.split(" "))  # Splits the string at the whitespace " ".

# isalpha() --> checks if alphabets only
print(str1.isalpha())

# isnumeric() --> checks numeric characters
print(str5.isnumeric())

# isalnum() --> The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9.
# If any other characters or punctuations are present, then it returns False.
print(str4.isalnum())

# index() --> returns index of substring
print(str3.find("python"))

# center() --> aligns the string to the center as per the parameters given by the user.
print(str3.center(50))
# We can also provide padding character. It will fill the rest with the fill characters provided by the user.
print(str3.center(50, "."))

# count() --> returns the number of times the given value has occurred within the given string.
print(str3.count("o"))

# startswith() --> checks if string starts with the specified string
print(str3.startswith("i"))
# We can even also check for a value in-between the string by providing start and end index positions.
print(str3.startswith("love", 2, 6))

# endswith() --> if the string ends with a given value. If yes, then return True, else return False.
print(str2.endswith("!"))
# We can even also check for a value in-between the string by providing start and end index positions.
print(str3.endswith("love", 2, 6))

# there are many more methods that can be used to perform modification on string.
# https://www.w3schools.com/python/python_strings_methods.asp

###########################################################################################

# Python - String Concatenation and formatting
# To concatenate, or combine, two strings you can use the + operator.

# Merge variable a with variable b into variable c:
a = "hello"
b = "world"
c = a + b
print(c)

# To add a space between them, add a " ":
d = a + " " + b
print(d)
print(a+" "+b)
print(a," ",b)

# we cannot join str and int using + operator, we get error
# TypeError: can only concatenate str (not "int") to str
name = "Alice"
age = 25
# print("My name is" + name + "and my age is" + age), this will get error

# Python lets you format strings to inject dynamic values into predefined text templates.
# Common formatting methods:
# Using %.
# using format().
# F-string literals.

# format() method.
# The format() methods places the arguments within the string
# wherever the placeholders are specified
statement = "My name is {} and my age is {}."
print(statement.format(name, age))
print("My name is {} and I am {} years old.".format(name, age))

# Using %
print("My name is %s and I am %d years old." % (name, age))

# Using string in curly braces, F-string literals.
print(f"My name is {name} and I am {age} years old.")

###########################################################################################

# Python - Escape Characters

# Escape Characters
# It is very important in python.
# It allows us to insert illegal characters into a string like a backslash, new line or a tab.
# Single/Double Quote: used to insert single/double quotes in the string.

# You will get an error if you use double quotes inside a string that is surrounded by double quotes:
# txt = "We are the so-called "Vikings" from the north."
# print(txt)

#The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# escape double quotes
example = "He said, \"What's there?\""
print(example)

# escape single quotes
example = 'He said, "What\'s there?"'
print(example)

# using triple quotes
print('''''They said, "What's there?"''')

# The list of an escape sequence is given below:
# \ ignores new line.
print("Python1 \
Python2 \
Python3")

# \\ ignores Backslash
print("\\")

# \' ignores Single Quotes
print('\'')

# \\'' ignoresDouble Quotes
print("\"")

# \a ignores ASCII Bell
print("\a")

# \b ignores ASCII Backspace(BS)
print("Hello \b World")

# \f ignores ASCII Formfeed
print("Hello \f World!")

# \n ignores ASCII Linefeed
print("Hello \n World!")

# \r ignores ASCII Carriege Return(CR)
print("Hello \r World!")

# \t ignores ASCII Horizontal Tab
print("Hello \t World!")

# \v ignores ASCII Vertical Tab
print("Hello \v World!")

# \ooo ignores Character with octal value
print("\110\145\154\154\157")

# \xHH ignores Character with hex value.
print("\x48\x65\x6c\x6c\x6f")

###########################################################################################

# Python Strings are immutable
# In Python, strings are immutable. That means the characters of a string cannot be changed. For example,

message = 'Hola Amigos'
message[0] = 'H'
print(message)

# However, we can assign the variable name to a new string. For example,
message = 'Hola Amigos'

# assign new string to message variable
message = 'Hello Friends'

print(message); # prints "Hello Friends"

###########################################################################################

# for more information, check
# https://www.javatpoint.com/python-strings



