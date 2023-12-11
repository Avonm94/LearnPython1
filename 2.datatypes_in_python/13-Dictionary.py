# Python Dictionaries
###########################################################################################
# Dictionaries are ordered collection of data items.
# They store multiple items in a single variable.
# Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# A dictionary is a collection that is ordered* (from python V3.7), changeable and do not allow duplicates.

# Example:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

# Example: Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford", "model": "Mustang",
  "year": 1964,"year": 2020
}
print(thisdict)

# ----------------------------------------------------------------------------------------
# Dictionary Length
# To determine how many items a dictionary has, use the len() function:
# Example:Print the number of items in the dictionary:
print(len(info))
print(len(thisdict))

###########################################################################################

# Create a Dictionary
# We create dictionaries by placing key:value pairs inside curly brackets {}, separated by commas.

# creating a dictionary

# ex:
country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Rome",
  "England": "London"
}
# printing the dictionary
print(country_capitals)

# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.
# Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Note: Dictionary keys must be immutable, such as tuples, strings, integers, etc.
# We cannot use mutable (changeable) objects such as lists as keys.

###########################################################################################

# Python - Access Dictionary Items

# I. Accessing single values:
# Values in a dictionary can be accessed using keys.
# We can access dictionary values by mentioning keys either in square brackets or by using get method.

# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))

# Ex:
country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Rome",
  "England": "London"
}
print(country_capitals["United States"])  # Washington D.C.
print(country_capitals["England"]) # London
# ----------------------------------------------------------------------------------------
# II. Accessing multiple values:
# We can print all the values in the dictionary using values() method.

# Example:
print(info.values())
print(country_capitals.values())
# ----------------------------------------------------------------------------------------
# III. Accessing keys:
# We can print all the keys in the dictionary using keys() method.
# Example:
print(info.keys())
print(country_capitals.keys())
# ----------------------------------------------------------------------------------------
# IV. Accessing key-value pairs:
# We can print all the key-value pairs in the dictionary using items() method.
# Example:
print(info.items())
print(country_capitals.items())

###########################################################################################

# Check if a Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:

# Example: Check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Example:
my_list = {1: "Hello", "Hi": 25, "Howdy": 100}
print(1 in my_list) # True
# the not in operator checks whether key doesn't exist
print("Howdy" not in my_list) # False
print("Hello" in my_list) # False

###########################################################################################

# Adding items to dictionary:
# There are two ways to add items to a dictionary.

# I. Create a new key and assign a value to it:
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info['DOB'] = 2001 # Adding key and value
print(info)

# Example :
country_capitals = {"United States": "Washington D.C.", "Italy": "Naples"}
print(country_capitals)

# add an item with "Germany" as key and "Berlin" as its value
country_capitals["Germany"] = "Berlin"
print(country_capitals)
# ----------------------------------------------------------------------------------------
# II. Use the update() method:
# The update() method updates the value of the key provided to it if the
# item already exists in the dictionary, else it creates a new key-value pair.

# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20}) # updating existing value using update()
info.update({'DOB':2001}) # adding item using update()
print(info)

###########################################################################################

# Removing items from dictionary:

# clear(): The clear() method removes all the items from the list.
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

info.clear()
print(info)
# ----------------------------------------------------------------------------------------
# pop(): The pop() method removes the key-value pair whose key is passed as a parameter.
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

info.pop('eligible')
print(info)
# ----------------------------------------------------------------------------------------
# popitem(): The popitem() method removes the last key-value pair from the dictionary.
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
print(info)

info.popitem()
print(info)
# ----------------------------------------------------------------------------------------
# del:apart from these three methods, we can also use the del keyword to remove a dictionary item.
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
print(info)

del info['age']
print(info)

###########################################################################################

# Copy Dictionaries

# We can use the copy() method to copy the contents of one dictionary into another dictionary.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
newDictionary = info.copy()
print(newDictionary)

# we can use the dict() function to make a new dictionary with the items of original dictionary.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
newDictionary = dict(info)
print(newDictionary)

###########################################################################################

# Loop Through a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)

# Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])

# You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)

# You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)

# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)

# Example:
country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Naples"
}

# print dictionary keys one by one
for country in country_capitals:
    print(country)

print("----------")

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)

###########################################################################################

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
# Example1:
myfamily = {
  "child1" : {"name" : "Emil","year" : 2004},
  "child2" : {"name" : "Tobias","year" : 2007},
  "child3" : {"name" : "Linus","year" : 2011}
}

print(myfamily)

# Or, if you want to add three dictionaries into a new dictionary:
# Example: Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {"name" : "Emil","year" : 2004}
child2 = {"name" : "Tobias","year" : 2007}
child3 = {"name" : "Linus","year" : 2011}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3}
print(myfamily)

# Access Items in Nested Dictionaries
# To access items from a nested dictionary; you use the name of the dictionaries, starting with the outer dictionary:
# Example: Print the name of child 2:
print(myfamily["child2"]["name"])

###########################################################################################
# -----------------------------------------------------------------------------------------

# Dictionaries methods

# clear() --> Removes all the elements from the dictionary
# copy() --> Returns a copy of the dictionary
# fromkeys() --> Returns a dictionary with the specified keys and value
# get() --> Returns the value of the specified key
# items() --> Returns a list containing a tuple for each key value pair
# keys() --> Returns a list containing the dictionary's keys
# pop() --> Removes the element with the specified key
# popitem() --> Removes the last inserted key-value pair
# setdefault() --> Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update() --> Updates the dictionary with the specified key-value pairs
# values() --> Returns a list of all the values in the dictionary

###########################################################################################
