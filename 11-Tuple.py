# Python Tuple Data type
# https://www.programiz.com/python-programming/tuple
###########################################################################################
# Python Tuple
# A tuple in Python is similar to a list.
# The difference between the two is that we cannot change the elements of a
# tuple once it is assigned, whereas we can change the elements of a list.
# A tuple is a collection that is ordered and unchangeable.
# They store multiple items in a single variable.
# items are separated by commas and enclosed within round brackets ().

# Tuples are an immutable data type, meaning their elements cannot be changed after they are generated.
# Each element in a tuple has a specific order that will never change because tuples are ordered sequences.

# ----------------------------------------------------------------------------------------

# Creating a Tuple,
# it is created by placing all the items (elements) inside parentheses (),
# separated by commas.
# The parentheses are optional, however, it is a good practice to use them.
# A tuple can have any number of items, and they may be of different types (integer, float, list, string, etc.).

# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

empty_tuple = ()
print("Empty tuple: ", empty_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

int_tuple = (4, 6, 8, 10, 12, 14)
print("Tuple with integers: ", int_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

mixed_tuple = (4, "Python", 9.3)
print("Tuple with different data types: ", mixed_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# Creating a nested tuple
nested_tuple = ("Python", {4: 5, 6: 2, 8: 2}, (5, 3, 5, 6))
print("A nested tuple: ", nested_tuple)

# As mentioned earlier, we can also create tuples without using parentheses:
my_tuple1 = 1, 2, 3
print(my_tuple1)

my_tuple2 = 1, "Hello", 3.4
print(my_tuple2)

# This is known as triple pressing.

# ----------------------------------------------------------------------------------------

# Create a Python Tuple With one Element
# In Python, creating a tuple with one element is a bit tricky.
# Having one element within parentheses is not enough.
# We will need a trailing comma to indicate that it is a tuple,

var1 = "hello"
print(type(var1))  # <class 'str'>

# Creating a tuple having one element
var2 = ("hello",)
print(type(var2))  # <class 'tuple'>

# Parentheses are optional
var3 = "hello",
print(type(var3))  # <class 'tuple'>

# ----------------------------------------------------------------------------------------

# Tuple Items:
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Ordered means that the items have a defined order, and that order will not change.
# Unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# ----------------------------------------------------------------------------------------

# Tuple Length
# To determine how many items a tuple has, use the len() function:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# ----------------------------------------------------------------------------------------

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.

thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)

###########################################################################################

# Tuple Indexes

# Each item/element in a tuple has its own unique index.
# This index can be used to access any particular item from the tuple.
# The first item has index [0], second item has index [1], third item has index [2] and so on.

# Positive indexing: always starts with 0
# Negative Indexing: always starts with -1

country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]    --> Positive Index
#            [-5]     [-4]    [-3]       [-2]      [-1]    --> Negative Index

# Positive
print(country[1])
print(country[3])
print(country[0])

# Negative
print(country[-1])
print(country[-3])
print(country[-4])

###########################################################################################

# Range of Index:Slicing

# You can print a range of tuple items by specifying where do you want to start,
# where do you want to end and if you want to skip elements in between the range.
# Syntax: Tuple[start : end : jumpIndex]
# Note:jump Index is optional. We will see this in given examples.

# Example: printing elements within a particular range:
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])  # using positive indexes
print(animals[-7:-2])  # using negative indexes

# Example: printing all elements from a given index till the end
print(animals[4:])  # using positive indexes
print(animals[-4:])  # using negative indexes

# Example: printing all elements from start to a given index
print(animals[:6])  # using positive indexes
print(animals[:-3])  # using negative indexes

# Example: print alternate values
print(animals[::2])  # using positive indexes
print(animals[-8:-1:2])  # using negative indexes

# Example: printing every 3rd consecutive withing given range
print(animals[0:8:3])
# Here, jump index is 3. Hence it prints every 3rd element within given index.
# includes start index

# ----------------------------------------------------------------------------------------

# We can access a range of items in a tuple by using the slicing operator colon :.

# accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# elements 2nd to 4th index
print(my_tuple[1:4])  # prints ('r', 'o', 'g')

# elements beginning to 2nd
print(my_tuple[:-7])  # prints ('p', 'r')

# elements 8th to end
print(my_tuple[7:])  # prints ('i', 'z')

# elements beginning to end
print(my_tuple[:])  # Prints ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

###########################################################################################

# Check if an Item Exists
# To determine if a specified item is present in a tuple use the in keyword:

# Example: Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# Ex
country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")

# Ex
country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")

# Ex
languages = ('Python', 'Swift', 'C++')
print('C' in languages)  # False
print('Python' in languages)  # True

###########################################################################################

# Python Tuple Methods

# In Python, methods that add items or remove items are not available with tuple.
# Only the following two methods are available.
# Some examples of Python tuple methods:

my_tuple = ('a', 'p', 'p', 'l', 'e',)
print(my_tuple.count('p'))  # prints 2
print(my_tuple.index('l'))  # prints 3

###########################################################################################

# Manipulating Tuples (Using Type Casting)
# Tuples are immutable, hence if you want to add, remove or change tuple items,
# then first you must convert the tuple to a list.
# Then perform the operation on that list and convert it back to tuple.

# Ex
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)  # Convert to List
temp.append("Russia")  # add item
temp.pop(3)  # remove item
temp[2] = "Finland"  # change item
countries = tuple(temp)  # converted to tuple
print(countries)

# Ex
# Example:Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# ----------------------------------------------------------------------------------------

# Add tuple to a tuple. You are allowed to add tuples to tuples,
# so if you want to add one item, (or many),
# create a new tuple with the item(s), and add it to the existing tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# ----------------------------------------------------------------------------------------
# we can directly concatenate two tuples instead of converting them to list and back.
# Ex
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2  # joined 2 tuples in one new variable
print(southEastAsia)

# Ex
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# ----------------------------------------------------------------------------------------

# Repetition Tuples in Python
# Python program to show repetition in tuples
tuple_ = ('Python', "Tuples")
print("Original tuple is: ", tuple_)
# Repeating the tuple elements
tuple_ = tuple_ * 3
print("New tuple is: ", tuple_)

# Ex
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

###########################################################################################

# Unpack Tuples
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# Unpacking is the process of assigning the tuple items as values to variables.

# ex
info = ("Marcus", 20, "MIT")  # Packing
(name, age, university) = info  # unpacking

print("Name:", name)
print("Age:", age)
print("Studies at:", university)

# ex
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print("Green: ", green)
print('Yellow: ', yellow)
print("Red: ", red)

# Note: The number of variables must match the number of values in the tuple,
# if not, you must use an asterisk to collect the remaining values as a list.

# ----------------------------------------------------------------------------------------

# Using Asterisk*,
# If the number of variables is less than the number of values,
# you can add an * to the variable name and the values will be assigned to the variable as a list:

# Ex: Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print("Green: ", green)
print('Yellow: ', yellow)
print("Red: ", red)

# If the asterisk is added to another variable name than the last,
# Python will assign values to the variable until the number of values left matches the number of variables left.

# Example: Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print("Green: ", green)
print('Tropic: ', tropic)
print("Red: ", red)

# Ex - 1
fauna = ("cat", "dog", "horse", "pig", "parrot", "salmon")
(*animals, bird, fish) = fauna

print("Animals:", animals)
print("Bird:", bird)
print("Fish:", fish)

# Ex - 2
fauna = ("parrot", "cat", "dog", "horse", "pig", "salmon")
(bird, *animals, fish) = fauna

print("Animals:", animals)
print("Bird:", bird)
print("Fish:", fish)

# Ex - 3
fauna = ("parrot", "salmon", "cat", "dog", "horse", "pig")
(bird, fish, *animals) = fauna

print("Animals:", animals)
print("Bird:", bird)
print("Fish:", fish)

###########################################################################################

# Iterating through a Tuple in Python,
# We can use for loop to iterate over the elements of a tuple. For example,
languages = ('Python', 'Swift', 'C++')
# iterating through the tuple
for language in languages:
    print(language)

###########################################################################################

# Tuples have the following advantages over lists:

# Triples take less time than lists do.
# Due to tuples, the code is protected from accidental modifications.
# It is desirable to store non-changing information in "tuples" instead of "records" if a program expects it.
# A tuple can be used as a dictionary key if it contains immutable
# values like strings, numbers, or another tuple.
# "Lists" cannot be utilized as dictionary keys because they are mutable.

# ----------------------------------------------------------------------------------------

# Advantages of Tuple over List in Python
# Since tuples are quite similar to lists, both of them are used in similar situations.

# However, there are certain advantages of implementing a tuple over a list:

# We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
# Since tuples are immutable, iterating through a tuple is faster than with a list.
# So there is a slight performance boost.
# Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
# If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

###########################################################################################