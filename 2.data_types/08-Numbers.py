# Python Numeric Data type
###########################################################################################
# In Python, numeric data type is used to hold numeric values.

# Integers, floating-point numbers and complex numbers fall under the Python numbers category. They are defined as int,
# float and complex classes in Python.

# int - holds signed integers of non-limited length.
# float - holds floating decimal points, and it's accurate up to 15 decimal places.
# complex - holds complex numbers.

num1 = 5
print(num1, 'is of type', type(num1))

num2 = 2.0
print(num2, 'is of type', type(num2))

num3 = 1 + 2j
print(num3, 'is of type', type(num3))

###########################################################################################
# Int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
# Example
# Integers:
x = 1
y = 35656222554887711
z = -3255522

print(x, type(x))
print(y, type(y))
print(z, type(z))

###########################################################################################
# Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
# Example
# Floats:

x = 1.10
y = 1.0
z = -35.59

print(x, type(x))
print(y, type(y))
print(z, type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
# Example
x = 35e3
y = 12E4
z = -87.7e100

print(x, type(x))
print(y, type(y))
print(z, type(z))

###########################################################################################
# Complex
# Complex numbers are written with a "j" as the imaginary part:
# Example
# Complex:

x = 3 + 5j
y = 5j
z = -5j

print(x, type(x))
print(y, type(y))
print(z, type(z))

###########################################################################################
# Type Conversion or Data Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:

# Example
# Convert from one type to another:
x = 1  # int
y = 2.99  # float
z = 1j  # complex

print(x, type(x))
print(y, type(y))
print(z, type(z))

# convert from int to float: we use float() function.
a = float(x)

# convert from float to int: we use int() function.
# int() function rounds of the given number to the nearest integer value.
b = int(y)

# convert from int to complex: we use the complex() function.
c = complex(x)
d = complex(y)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
# Note: You cannot convert complex numbers into another number type.

###########################################################################################
# Random Number
# Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to make random numbers:
# Example

# Import the random module, and display a random number between 1 and 9:
import random

print(random.randrange(1, 10))

# Everytime it will print random number
