# Python List Data type
# https://www.programiz.com/python-programming/list
###########################################################################################
# List:
# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation. Or
# Lists are mutable (changeable). Meaning we can add and remove elements from a list.

# Ex1
lst1 = [1, 2, 2, 3, 5, 4, 6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)

# Ex
details = ["Avinash", 18, "FYBScIT", 9.8]
print(details)

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.
# Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)

# As we can see, a single list can contain items of different datatypes.
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# ---------------------------------------------------------------------------

# To get length of a list we use len().
print(len(thislist))

# ---------------------------------------------------------------------------

# We can concat the lists using +
lst1 = [1, 2, 2, 3, 5, 4, 6]
lst2 = ["Red", "Green", "Blue"]
print(lst1 + lst2)
print(lst2 + lst1)

print(lst1, lst2)  # this will print lists in one line.

###########################################################################################

# List Indexes

# Each item/element in a list has its own unique index.
# This index can be used to access any particular item from the list.

# Positive Index:
# The first item has index [0], the second item has index [1], the third item has index [2] and so on.

# Negative Index:
# The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

# Example:
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]   --> Positive Index
#          [-5]    [-4]    [-3]     [-2]      [-1]  --> Negative Index

# length of a list
print(len(colors))

# Positive Index:
print(colors[2])
print(colors[4])
print(colors[0])

# Negative Index:
print(colors[-1])
print(colors[-3])
print(colors[-5])

###########################################################################################
# Range of Index:

# You can print a range of list items by specifying where you want to start,
# where you want to end, and if you want to skip elements in between the range.
# Syntax: List[start : end : jumpIndex]
# Note: jump Index is optional. We will see this in given examples.

# printing elements within a particular range:
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# length of a list
print(len(animals))

print(animals[3:7])  # using positive indexes
print(animals[-7:-2])  # using negative indexes

# Here, we provide index of the element from where we want to start
# and the index of the element till which we want to print the values.
# Note: The element of the end index provided will not be included.

# printing all elements from a given index till the end
print(animals[4:])  # using positive indexes
print(animals[-4:])  # using negative indexes
# When no end index is provided, the interpreter prints all the values till the end

# printing all elements from start to a given index
print(animals[:6])  # using positive indexes
print(animals[:-3])  # using negative indexes
# When no start index is provided, the interpreter prints all the values from start up to the end index provided.

# print alternate values
print(animals[::2])  # using positive indexes
print(animals[-8:-1:2])  # using negative indexes
# Here, we have not provided start and index, which means all the values will be considered.
# But as we have provided a jump index of 2 only alternate values will be printed.

# printing every 3rd consecutive withing given range
print(animals[1:8:3])
# Here, jump index is 3. Hence it prints every 3rd element within given index.

###########################################################################################
# Check for item:
# We can check if a given item is present in the list. This is done using the in keyword.

# Ex1
languages = ['Python', 'Swift', 'C++']
print('C' in languages)  # False
print('Python' in languages)  # True

# Ex2
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")

if "Orange" in colors:
    print("Orange is present.")
else:
    print("Orange is absent.")

#  Ex3
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

###########################################################################################

# Add List Items
# there are three methods to add items to list: append(), insert() and extend().
# remember the length of the list will be increased.

# append():
# This method appends items to the end of the existing list.

colors = ["violet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.append("green")
print(colors)

# ---------------------------------------------------------------------------

# insert():
# This method inserts an item at the given index. User has to specify index and the item
# to be inserted within the insert() method.

colors.insert(1, "green")  # inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)

# Example
# Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# ---------------------------------------------------------------------------

# extend():
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

# add a list to a list
colors = ["violet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)

# add a tuple to a list
cars = ["Hyundai", "Tata", "Mahindra"]
cars2 = ("Mercedes", "Volkswagen", "BMW")
cars.extend(cars2)
print(cars)

# add a set to a list
cars = ["Hyundai", "Tata", "Mahindra"]
cars2 = {"Mercedes", "Volkswagen", "BMW"}
cars.extend(cars2)
print(cars)

# add a dictionary to a list
students = ["Sakshi", "Aaditya", "Ritika"]
students2 = {"Yash": 18, "Devika": 19, "Soham": 19}  # only add keys, does not add values
students.extend(students2)
print(students)

###########################################################################################

# Remove List Items
# There are various methods to remove items from the list: pop(), remove(), del(), clear()
# remember the length of the list will be decreased.

# pop():
# This method removes the last item of the list if no index is provided.
# If an index is provided, then it removes item at that specified index.
# Example 1:
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
colors.pop()  # removes the last item of the list
print(colors)

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
colors.pop(1)  # removes item at index 1
print(colors)

# ---------------------------------------------------------------------------

# remove():
# This method removes specific item from the list.
# Example:
colors = ["violet", "indigo", "blue", "green", "yellow"]
colors.remove("blue")

# Example
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
# remove 'Python' from the list
languages.remove('Python')
print(languages)  # ['Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# ---------------------------------------------------------------------------

# del:
# del is not a method, rather it is a keyword which deletes item at specific
# from the list, or deletes the list entirely.

# Example 1:
colors = ["violet", "indigo", "blue", "green", "yellow"]
del colors[3]
print(colors)

# Example 2:
colors = ["violet", "indigo", "blue", "green", "yellow"]
del colors
# print(colors)
# NameError: name 'colors' is not defined
# We get an error because our entire list has been deleted and there is no variable called colors which contains a list.

# Example 3:
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the second item
del languages[1]
print(languages)  # ['Python', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the last item
del languages[-1]
print(languages)  # ['Python', 'C++', 'C', 'Java', 'Rust']

# delete the first two items
del languages[0: 2]  # ['C', 'Java', 'Rust']
print(languages)

# ---------------------------------------------------------------------------

# clear():
# This method clears all items in the list and prints an empty list.
# Example:
colors = ["violet", "indigo", "blue", "green", "yellow"]
colors.clear()
print(colors)

###########################################################################################

# Change List Items
# Changing items from a list is easier, you just have to specify the index where you
# want to replace the item with existing item.
# remember, the length of the list will be increased or decreased accordingly.

# Example:
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
print(names)

# replacing item
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2] = "Millie"
print(names)

# ---------------------------------------------------------------------------

# You can also change more than a single item at once.
# To do this, just specify the index range over which you want to change the items.
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
print(names)
print(len(names))
names[2:4] = ["juan", "Anastasia"]
print(names)
print(len(names))

# ---------------------------------------------------------------------------

# What if the range of the index is more than the list of items provided?
# In this case, all the items within the index range of the original list are replaced by the items that are provided
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
print(names)
print(len(names))
names[1:4] = ["juan", "Anastasia"]
print(names)
print(len(names))

# What if we have more items to be replaced than the index range provided?
# In this case, the original items within the range are replaced by the new items
# and the remaining items move to the right of the list accordingly.
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
print(names)
print(len(names))
names[2:3] = ["juan", "Anastasia", "Bruno", "Olga", "Rosa"]
print(names)
print(len(names))

# ---------------------------------------------------------------------------

# If you insert more items than you replace,
# the new items will be inserted where you specified, and the remaining items will move accordingly:

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))

# Change the second value by replacing it with two new values:
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
print(len(thislist))

# If you insert less items than you replace, the new items will be inserted where you specified,
# and the remaining items will move accordingly:

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))

# Change the second and third value by replacing it with one value:
thislist[1:3] = ["watermelon"]
print(thislist)
print(len(thislist))

# Note: The length of the list will change when the number of items
# inserted does not match the number of items replaced.

###########################################################################################

# Slicing of a List
# In Python, it is possible to access a portion of a list using the slicing operator.

my_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

# items from index 2 to index 4
print(my_list[2:5])
# my_list[2:5] returns a list with items from index 2 to index 4.

# items from index 5 to end
print(my_list[5:])
# my_list[5:] returns a list with items from index 5 to the end.

# items beginning to end
print(my_list[:])
# my_list[:] returns all list items

# Note: When we slice lists, the start index is inclusive, but the end index is exclusive.

###########################################################################################

# List Comprehension
# List comprehensions are used for creating new lists from
# other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
# It is a concise and elegant way to create lists. For example,

# Syntax:
# List = [expression(item) for item in iterable if condition]
# expression: it is the item which is being iterated.
# iterable: it can be list, tuples, dictionaries, sets, and even in arrays and strings.
# condition: condition checks if the item should be added to the new list or not.

# Ex1:accepts items with the small letter “o” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

# Ex2: accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)

# Ex3: create a list with value n ** 2 where n is a number from 1 to 5
numbers = [n ** 2 for n in range(1, 6)]
print(numbers)  # Output: [1, 4, 9, 16, 25]

# Here, this code is equivalent to

numbers = []
for n in range(1, 6):
    numbers.append(n ** 2)
# https://www.w3schools.com/python/python_lists_comprehension.asp
###########################################################################################

# Iterating through a List

# We can use a for loop to iterate over the elements of a list. For example,
languages = ['Python', 'Swift', 'C++']
# iterating through the list
for language in languages:
    print(language)

# iteration of the list
# declaring the list
list1 = [12, 14, 16, 39, 40]
# iterating
for i in list1:
    print(i)

# iterating a list
list = ["John", "David", "James", "Jonathan"]
for i in list:
    # The i variable will iterate over the elements of the List and contains each element in each iteration.
    print(i)

###########################################################################################

# Repetition of list
# The redundancy administrator empowered the rundown components to be rehashed on different occasions.

# declaring the list
list1 = [12, 14, 16, 18, 20]
print(list1)

# repetition operator *
l = list1 * 2  # new list with repetition
print(l)

list2 = ['a', 'b', 'c', 'd']
print(list2)
l1 = list2 * 3
print(l1)

###########################################################################################

# Python List Built-in Functions

# len( ):It is used to calculate the length of the list.
# size of the list
# declaring the list
list1 = [12, 16, 18, 20, 39, 40]
# finding length of the list
len(list1)

# ---------------------------------------------------------------------------

# Max( ):It returns the maximum element of the list
# maximum of the list
list1 = [103, 675, 321, 782, 200]
# large element in the list
print(max(list1))

list2 = ['A', 'B', 'C', 'D']
print(max(list2))

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
print(max(names))

# ---------------------------------------------------------------------------

# Min( ):It returns the minimum element of the list
# minimum of the list
list1 = [103, 675, 321, 782, 200]
# smallest element in the list
print(min(list1))

list2 = ['A', 'B', 'C', 'D']
print(min(list2))

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
print(min(names))

###########################################################################################

# List Methods
# We have discussed methods like append(), clear(), extend(), insert(), pop(), remove() before.
# Now we will learn about some more list methods:

# sort(): This method sorts the list in ascending order.
# Example 1:

colors = ["violet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4, 2, 5, 3, 6, 1, 2, 1, 2, 8, 9, 7]
num.sort()
print(num)

# What if you want to print the list in descending order?
# We must give reverse=True as a parameter in the sort method.

colors = ["violet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)

num = [4, 2, 5, 3, 6, 1, 2, 1, 2, 8, 9, 7]
num.sort(reverse=True)
print(num)

# The reverse parameter is set to False by default.

# Note: Do not mistake the reverse parameter with the reverse method.
# ---------------------------------------------------------------------------
# reverse(): This method reverses the order of the list.

colors = ["violet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

num = [4, 2, 5, 3, 6, 1, 2, 1, 2, 8, 9, 7]
num.reverse()
print(num)
# ---------------------------------------------------------------------------
# index(): This method returns the index of the first occurrence of the list item.

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4, 2, 5, 3, 6, 1, 2, 1, 3, 2, 8, 9, 7]
print(num.index(3))
# ---------------------------------------------------------------------------
# count(): Returns the count of the number of items with the given value.

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

num = [4, 2, 5, 3, 6, 1, 2, 1, 3, 2, 8, 9, 7]
print(num.count(2))
# ---------------------------------------------------------------------------
# copy(): Returns copy of the list.
# This can be done to perform operations on the list without modifying the original list.

colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)

###########################################################################################

# Method --> Description
# append() --> add an item to the end of the list
# extend() --> add all the items of an iterable to the end of the list
# insert() --> inserts an item at the specified index
# remove() --> removes item present at the given index
# pop() --> returns and removes item present at the given index
# clear() --> removes all items from the list
# index() --> returns the index of the first matched item
# count() --> returns the count of the specified item in the list
# sort() --> sort the list in ascending/descending order
# reverse() --> reverses the item of the list
# copy() --> returns the shallow copy of the list

###########################################################################################