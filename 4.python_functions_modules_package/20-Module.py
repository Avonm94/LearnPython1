# Python Modules
###########################################################################################
# python modules are python (.py) files that contain python code that we can use within our python files
# ensuring simplicity and code reusability.

# module --> collection of functions and variables.

# Built in Modules (Standard Modules):
# Python's standard library comes bundled with a large number of modules.
# They are called built-in modules. Most of these built-in modules are written in
# C (as the reference implementation of Python is in C), and pre-compiled into the library.
# These modules pack useful functionality like system-specific OS management, disk IO, networking, etc.

# Here are some popular python built-in modules:
# csv, datetime, json, math, random, sqlite3, statistics, tkinter, turtle, etc.
# check other on below link
# https://docs.python.org/3/py-modindex.html

# -----------------------------------------------------------------------------------------

# User Defined Modules
# Any text file with .py extension and containing Python code is basically a module.
# It can contain definitions of one or more functions, variables, constants as well as classes.
# Any Python object from a module can be made available to interpreter session or
# another Python script by import statement. A module can also include runnable code.

# Let us create a module. Type the following and save it as calculator.py.
# you can find it in this same folder

import calculator

calculator.add(1, 1)
calculator.mul(1, 1)
calculator.sub(1, 1)
calculator.div(2, 1)

# -----------------------------------------------------------------------------------------


# How to use module
#  to use any modules first, we have to import them into this particular file using import or from kw.

# The import Statement
# import <module_name>
# from <module_name> import <name(s)>
# from <module_name> import <name> as <alt_name> (alias name)
# import <module_name> as <alt_name>

# -----------------------------------------------------------------------------------------

# Built in module

# Ex1: import <module_name>
import math

# To check functions present in above-imported module we'll use dir() function.
print(dir(math))  # this will print all the functions present in math module.
# or
# x = dir(math)  # created a new list variable and passing math (name) through dir().
# print(x)  # this will print all the functions present in math module
# Note: The dir() function can be used on all modules, also the ones you create yourself.


# using the functions from modules:

a = math.sqrt(25)
print(a)

b = math.pi
print('Value of Pi', b)

# -----------------------------------------------------------------------------------------

# import <module_name> as <alt_name>
import calculator as cal

cal.add(1, 3)

import math as m

print(m.sqrt(25))

# -----------------------------------------------------------------------------------------

# from <module_name> import <name(s)>
# We can import specific names from a module without importing the module as a whole.

from calculator import add

add(2, 3)

from math import sqrt

print(sqrt(144))

# for this approach, we don't write m<module_name>.<name> while using.

# -----------------------------------------------------------------------------------------
###########################################################################################

# External Modules
# these must be downloaded from outside.
# They don't exist yet like the built-in ones.
# Installing them is a basic task and can be done using
# the "pip install module_name" command in the compiler terminal.

###########################################################################################

# Examples with class

# Approach 1
import animal as a
import bird as b

dog = a.Animal()
dog.display('dog')
dog.run()

sparrow = b.Bird()
sparrow.display('Sparrow')
sparrow.fly()

# Approach 2
from animal import Animal
from bird import Bird

cat = Animal()
cat.display('cat')
cat.run()

crow = Bird()
crow.display('crow')
crow.fly()


###########################################################################################

# https://realpython.com/python-modules-packages/

###########################################################################################
