# Python Type Casting/Conversion
# and user input
###########################################################################################
# In programming, type conversion is the process of converting data of one type to another.
# For example, converting int data to str.

# There are two types of type conversion in Python.
# 1.Implicit Conversion - automatic type conversion
# 2.Explicit Conversion - manual type conversion
# ----------------------------------------------------------------------------------------
# 1.Python Implicit Type Conversion

# In certain situations, Python automatically converts one data type to another.
# This is known as implicit type conversion.

# Example 1: Converting integer to float
# Let's see an example where Python promotes the conversion of the lower data type (integer)
# to the higher data type (float) to avoid data loss.

integer_number = 123
float_number = 1.23
print(integer_number)
print(float_number)

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:", new_number)
print("Data Type:", type(new_number))

# In the above example, we have created two variables:
# integer_number and float_number of int and float type respectively.
# Then we added these two variables and stored the result in new_number.
# As we can see new_number has value 124.23 and is of the float data type.
# It is because Python always converts smaller data types to larger data types to avoid the loss of data.

# Note:
# We get TypeError, if we try to add str and int. For example, '12' + 23.
# Python is not able to use Implicit Conversion in such conditions.
# Python has a solution for these types of situations which is known as Explicit Conversion.

# ----------------------------------------------------------------------------------------

# 2.Python Explicit Type Conversion

# In Explicit Type Conversion, users convert the data type of an object to required data type.
# We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion.
# This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.

# Example 2: Addition of string and integer Using Explicit Conversion
num_string = '12'
num_integer = 23
print("Data type of num_string before Type Casting:", type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:", type(num_string))

num_sum = num_integer + num_string

print("Sum:", num_sum)
print("Data type of num_sum:", type(num_sum))

# In the above example, we have created two variables: num_string
# and num_integer with str and int type values respectively. Notice the code,
# num_string = int(num_string)
# Here, we have used int() to perform explicit type conversion of num_string to an integer type.
# After converting num_string to an integer value, Python is able to add these two variables.
# Finally, we got the num_sum value i.e 35 and data type to be int.
###########################################################################################

# Key Points to Remember
# Type Conversion is the conversion of an object from one data type to another data type.
# Implicit Type Conversion is automatically performed by the Python interpreter.
# Python avoids the loss of data in Implicit Type Conversion.
# Explicit Type Conversion is also called Type Casting, the data types of objects are
# converted using predefined functions by the user.
# In Type Casting, loss of data may occur as we enforce the object to a specific data type.

###########################################################################################

# Note:
# user input is considered as str value.

###########################################################################################

# We can get user's input from console using input() method

# Ex
name = input("enter your name:")
print(name)
print(type(name))

# Ex: addition of 2 numbers
num1 = input("enter num1:")  # 100
num2 = input("enter num2:")  # 200

sum1 = num1 + num2  # in this line input acts as string + operator will concatenate them
print(sum1)  # 100200
print("type of sum1: ", type(sum1))

sum2 = int(num1) + int(num2)  # in this line input is converted to integer, the summation will happen.
print(sum2) # 300
print("type of sum2: ", type(sum2))


num3 = int(input("enter num3:") ) # 100
num4 = int(input("enter num4:") )# 200
# in the above code python take user's input as str, convert it to int and stores in variable

print("type of num3",type(num3))
print("type of num4",type(num4))

sum3 = num3 + num4
print(sum3)
print("type of sum3: ", type(sum3))

###########################################################################################
a = 10
b = 20
c = 10.10
d = "20"
e = "20"

print(a+b)
print(a+c)
# print(a+d)
print(d+e)
###########################################################################################