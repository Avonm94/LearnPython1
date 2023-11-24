# Python Data Types
###########################################################################################
# Data Types --> Classes --> Description

# Numeric --> int, float, complex --> holds numeric values
# int: 3, -8, 0
# float: 7.349, -9.0, 0.0000001
# complex: 6 + 2i

# String --> str --> holds a sequence of characters
# str: “Hello World!!!”, “Python Programming”

# Sequence --> list, tuple, range --> holds a collection of items
# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets.
# Lists are mutable and can be modified after creation.

# tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses.
# Tuples are immutable and can not be modified after creation.

# range: returns a sequence of numbers as specified by the user.
# If not specified by the user then it starts from 0 by default and increments by 1.

# Mapping --> dict --> holds data in key-value pair form
# dict: a dictionary is an unordered collection of data containing a key:value pair.
# The key:value pairs are enclosed within curly brackets.

# Boolean --> bool --> holds either True or False

# Set --> set, frozeenset --> hold collection of unique items
# Set is an unordered collection of elements in which no element is repeated.
# The elements of sets are separated by a comma and contained within curly braces.

#Binary -->  bytes, bytearray, memoryview --> holds binary values
# bytes: bytes() function is used to convert objects into byte objects,
# or create empty bytes object of the specified size.

# bytearray: bytearray() function is used to convert objects into bytearray objects,
# or create empty bytearray object of the specified size.

# memoryview: memoryview() function returns a memory view object from a specified object.

# None:
# None is used to define a null value. When we assign a None value to a variable, we are essentially
# resetting it to its original empty state which is not the same as zero, an empty string or a False value.

# Since everything is an object in Python programming,
# data types are actually classes and variables are instances(object) of these classes.
###########################################################################################

# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:
# Text Type:str
# Numeric Types:int, float, complex
# Sequence Types:list, tuple, range
# Mapping Type:dict
# Set Types:set, frozenset
# Boolean Type:bool
# Binary Types:bytes, bytearray, memoryview
# None Type:NoneType

# Getting the Data Type
# You can get the data type of any object by using the type() function:

# Print the data type of the variable x:
x = 5
print(type(x))

###########################################################################################
# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:

x = "Hello World"  # str
print("The value present in x: ", x, " the data type is ", type(x))

x = 20  # int
print("The value present in x: ", x, " the data type is ", type(x))

x = 20.5  # float
print("The value present in x: ", x, " the data type is ", type(x))

x = 1j  # complex
print("The value present in x: ", x, " the data type is ", type(x))

x = ["apple", "banana", "cherry"]  # list
print("The value present in x: ", x, " the data type is ", type(x))

x = ("apple", "banana", "cherry")  # tuple
print("The value present in x: ", x, " the data type is ", type(x))

x = range(6)  # range
print("The value present in x: ", x, " the data type is ", type(x))

x = {"name": "John", "age": 36}  # dict
print("The value present in x: ", x, " the data type is ", type(x))

x = {"apple", "banana", "cherry"}  # set
print("The value present in x: ", x, " the data type is ", type(x))

x = frozenset({"apple", "banana", "cherry"})  # frozenset
print("The value present in x: ", x, " the data type is ", type(x))

x = True  # bool
print("The value present in x: ", x, " the data type is ", type(x))

x = b"Hello"  # bytes
print("The value present in x: ", x, " the data type is ", type(x))

x = bytearray(5)  # bytearray
print("The value present in x: ", x, " the data type is ", type(x))

x = memoryview(bytes(5))  # memoryview
print("The value present in x: ", x, " the data type is ", type(x))

x = None  # NoneType
print("The value present in x: ", x, " the data type is ", type(x))

###########################################################################################

# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

x = str("Hello World")  # str
print("The value present in x: ", x, " the data type is ", type(x))

x = int(20)  # int
print("The value present in x: ", x, " the data type is ", type(x))

x = float(20.5)  # float
print("The value present in x: ", x, " the data type is ", type(x))

###########################################################################################

# other examples

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

sequence1 = range(4,14,2)
for i in sequence1:
    print(i)

dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)

#Converting string to bytes
str1 = "This is a string"
arr1 = bytes(str1, 'utf-8')
print(arr1)
arr2 = bytes(str1, 'utf-16')
print(arr2)

#Creating bytes of given size
bytestr = bytes(4)
print(bytestr)

#Converting string to bytes
str1 = "This is a string"
arr1 = bytearray(str1, 'utf-8')
print(arr1)
arr2 = bytearray(str1, 'utf-16')
print(arr2)

#Creating bytes of given size
bytestr = bytearray(4)
print(bytestr)

str1 = bytes("home", "utf-8")
memoryviewstr = memoryview(str1)
print(list(memoryviewstr[0:]))

set1 = {4, -5, 8, 3, 2.9}
print(set1)

state = None
print(type(state))

###########################################################################################

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection that is ordered and changeable. Allows duplicate members.
# Tuple is a collection that is ordered and unchangeable. Allows duplicate members.
# Set is a collection that is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection that is ordered** and changeable. No duplicate members.

# *Set items are unchangeable, but you can remove and/or add items whenever you like.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered
###########################################################################################