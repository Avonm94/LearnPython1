# Python Set Data type
###########################################################################################
# Sets are unordered collection of data items.
# They store multiple items in a single variable.
# Sets items are separated by commas and enclosed within curly brackets {}.
# Sets are unchangeable, meaning you cannot change items of the set once created.
# Sets do not contain duplicate items.

# Once a set is created, you cannot change its items, but you can remove items and add new items.


info = {"Carla", 19, False, 5.9, 19}
print(info)

# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

# Here we see that the items of set occur in random order, and hence,
# they cannot be accessed using index numbers. Also, sets do not allow duplicate values.

# Note: In set The values True and 1,False and 0 are considered as same and treated as duplicate.

thisset = {"apple", "banana", "cherry", "banana", True, 1, 2, False, 0}
print(thisset)

###########################################################################################

# Find Number of Set Elements

# We can use the len() method to find the number of elements present in a Set. For example,
even_numbers = {2, 4, 6, 8}
print('Set:', even_numbers)
#
# find number of elements
print('Total Elements:', len(even_numbers))

###########################################################################################

# Create an Empty Set in Python

# Creating an empty set is a bit tricky. Empty curly braces {} will make an empty dictionary in Python.
# To make a set without any elements, we use the set() function without any argument. For example,

# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = {}

# check data type of empty_set
print('Data type of empty_set:', type(empty_set))

# check data type of dictionary_set
print('Data type of empty_dictionary', type(empty_dictionary))

###########################################################################################

# Accessing set items:

# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or
# ask if a specified value is present in a set, by using the in keyword.
# Example:
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)

# Example:Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# Example: Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

###########################################################################################

# Add and Update Set Items in Python

# Sets are mutable. However, since they are unordered, indexing has no meaning.
# We cannot access or change an element of a set using indexing or slicing.
# Set data type does not support it.

# Add Items to a Set in Python
# In Python, we use the add() method to add an item to a set. For example,

numbers = {21, 34, 54, 12}
print('Initial Set:', numbers)

# # using add() method
numbers.add(32)

print('Updated Set:', numbers)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
print(cities)

cities.add("Helsinki")
print(cities)

# ----------------------------------------------------------------------------------------

# Update Python Set

# The update() method is used to update the set with items
# other collection types (lists, tuples, sets, etc). For example,

companies = {'Lacoste', 'Ralph Lauren'}
print(companies)
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

###########################################################################################

# Remove Item

# To remove an item in a set, use the remove(), or the discard() method.

# Example 1:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
print(cities)
cities.remove("Tokyo")
print(cities)
cities.discard("Delhi")
print(cities)

# The main difference between remove and discard is that, if we try to delete an item which is not present in set,
# then remove() raises an error, whereas discard() does not raise any error.

# ----------------------------------------------------------------------------------------

# You can also use the pop() method to remove an item,
# but this method will remove a random item,
# so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.

#  Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# Ex1
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
print(cities)
item = cities.pop()
print(cities)
print(item)

# Ex2
thisset = {"apple", "banana", "cherry"}
print(thisset)
x = thisset.pop()
print(x)
print(thisset)

# ----------------------------------------------------------------------------------------

# del:
# del is not a method, rather it is a keyword which deletes the set entirely.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities) # Output:NameError: name 'cities' is not defined

# ----------------------------------------------------------------------------------------

# clear():
# This method clears all items in the set and prints an empty set.
# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

###########################################################################################

# Check if item exists

# You can also check if an item exists in the set or not.
# Example 1:
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")

# Example 2:
info = {"Carla", 19, False, 5.9}
if "Carmen" in info:
    print("Carmen is present.")
else:
    print("Carmen is absent.")

###########################################################################################

# Set joins & operators:

# Sets in python more or less work in the same way as sets in mathematics.
# We can perform operations like union and intersection on the sets just like in mathematics.

# I. union() and update():
# The union() and update() methods prints all items that are present in the two sets.
# The union() method returns a new set whereas update() method adds item into the existing set from another set.
# We use the | operator or the union() method to perform the set union operation.

# Example 1:
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print("cities1: ", cities1)
print("cities2: ", cities2)

cities3 = cities1.union(cities2)  # union
print("Union of cities1 & cities2: ", cities3)

cities1.update(cities2)  # update
print("Update cities1 & cities2: ", cities1)

# Example 2:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

print("set1:", set1)
print("set2:", set1)

set3 = set1.union(set2)  # union
print("union of set1 & set2:", set3)

set1.update(set2)  # update
print("update set1 adding  set2: ", set1)

# Both union() and update() will exclude any duplicate items.

# Example 3:

A = {1, 3, 5}  # first set
B = {0, 2, 4}  # second set
print('Union using |:', A | B)  # perform union operation using |
print('Union using union():', A.union(B))  # perform union operation using union()

# ----------------------------------------------------------------------------------------

# II. intersection and intersection_update():
# The intersection() and intersection_update() methods prints only items that are similar to both the sets.
# The intersection() method returns a new set whereas intersection_update() method updates into
# the existing set from another set.
# we use the & operator or the intersection() method to perform the set intersection operation.

# Example 1:
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print("cities1: ", cities1)
print("cities2: ", cities2)

cities3 = cities1.intersection(cities2)
print("intersection: ", cities3)  # intersection

cities1.intersection_update(cities2)  # intersection_update()
print("Intersection Update cities1 & cities2: ", cities1)

# Example 2:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(x)
print(y)

z = x.intersection(y)  # intersection
print("Intersection: ", z)

x.intersection_update(y)  # intersection_update()
print("Intersection_update: ", x)

# The intersection() method will return a new set, that only contains the items that are present in both sets.
# The intersection_update() method will keep only the items that are present in both sets.

# Example 3:
A = {1, 3, 5}  # first set
B = {1, 2, 4}  # second set
print('Intersection using &:', A & B)  # perform intersection operation using &
print('Intersection using intersection():', A.intersection(B))  # perform intersection operation using intersection()

# ----------------------------------------------------------------------------------------

# III. difference() and difference_update():
# The difference() and difference_update() methods prints only items that are
# only present in the original set and not in both the sets.
# The difference() method returns a new set whereas difference_update() method updates
# into the existing set from another set.
# We use the - operator or the difference() method to perform the difference between two sets.

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print("difference: ", cities3)

# Example:
A = {1, 3, 5}  # first set
B = {1, 2, 4}  # second set

print('Difference using &:', A - B)  # perform difference operation using &
print('Difference using difference():', A.difference(B))  # perform difference operation using difference()

# ----------------------------------------------------------------------------------------

# III. symmetric_difference and symmetric_difference_update():
# The symmetric_difference() and symmetric_difference_update() methods
# prints only items that are not similar to both the sets.
# The symmetric_difference() method returns a new set whereas symmetric_difference_update()
# method updates into the existing set from another set.
# In Python, we use the ^ operator or the symmetric_difference() method
# to perform symmetric difference between two sets.

# Example:
A = {2, 3, 5} # first set
B = {1, 2, 6} # second set
print('using ^:', A ^ B) # perform difference operation using &
print('using symmetric_difference():', A.symmetric_difference(B)) # using symmetric_difference()

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
cities.symmetric_difference_update(cities2)
print(cities)

# ----------------------------------------------------------------------------------------

# Check if two sets are equal,
# We can use the == operator to check whether two sets are equal or not. For example,

A = {1, 3, 5} # first set
B = {3, 5, 1} # second set

# perform difference operation using &
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')

###########################################################################################
# ----------------------------------------------------------------------------------------

# Set Methods

# add() --> Adds an element to the set
# clear() --> Removes all elements from the set
# copy() --> Returns a copy of the set
# difference() --> Returns the difference of two or more sets as a new set
# difference_update() --> Removes all elements of another set from this set
# discard() --> Removes an element from the set if it is a member. (Do nothing if the element is not in set)
# intersection() --> Returns the intersection of two sets as a new set
# intersection_update() --> Updates the set with the intersection of itself and another
# isdisjoint() --> Returns True if two sets have a null intersection
# issubset() --> Returns True if another set contains this set
# issuperset() --> Returns True if this set contains another set
# pop() --> Removes and returns an arbitrary set element. Raises KeyError if the set is empty
# remove() --> Removes an element from the set. If the element is not a member, raises a KeyError
# symmetric_difference() --> Returns the symmetric difference of two sets as a new set
# symmetric_difference_update() --> Updates a set with the symmetric difference of itself and another
# union() --> Returns the union of sets in a new set
# update() --> Updates the set with the union of itself and others

###########################################################################################