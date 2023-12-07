# Python polymorphism
# poly - many, morphs - forms
# The same object or thing changing its state from one form to another is known as polymorphic.
# The same function or method, being used differently in different scenarios,
# can perfectly describe Polymorphism. It occurs mostly with base and derived classes.
# In python, polymorphism is achieved by using Duck typing, method/operator overriding, and overloading.

###########################################################################################

# Example 1: Polymorphism in addition operator (Operator Overloading)
# We know that the + operator is used extensively in Python programs. But, it does not have a single usage.
# For integer data types, + operator is used to perform arithmetic addition operation

num1 = 1
num2 = 2
print(num1 + num2)

# Similarly, for string data types, + operator is used to perform concatenation.

str1 = "Python"
str2 = "Programming"
print(str1 + " " + str2)

# Here, we can see that a single operator + has been used to carry out different operations
# for distinct data types. This is one of the most simple occurrences of polymorphism in Python.

# -----------------------------------------------------------------------------------------

# Function Polymorphism in Python
# There are some functions in Python which are compatible to run with multiple data types.
# One such function is the len() function. It can run with many data types in Python.

# Example 2: Polymorphic len() function

print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))


# Here, we can see that many data types such as string, list, tuple, set, and dictionary can work with the len() function.
# However, we can see that it returns specific information about specific data types.

# -----------------------------------------------------------------------------------------

# We can use the concept of polymorphism while creating class methods as Python allows different classes to have methods
# with the same name.
# We can then later generalize calling these methods by disregarding the object we are working with.

# Example 3: Polymorphism in Class Methods

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.info()
    animal.make_sound()


# Here, we have created two classes Cat and Dog. They share a similar structure
# and have the same method names info() and make_sound().
# However, notice that we have not created a common superclass or
# linked the classes together in any way. Even then, we can pack these two different objects
# into a tuple and iterate through it using a common animal variable. It is possible due to polymorphism.

# -----------------------------------------------------------------------------------------

# Polymorphism and Inheritance
# The child classes in Python also inherit methods and attributes from the parent class.
# We can redefine certain methods and attributes specifically to fit the child class,
# which is known as Method Overriding.
# Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class.

# Method Overriding

class Bank:
    def getroi(self):
        return 10


class SBI(Bank):
    def getroi(self):
        return 7


class ICICI(Bank):
    def getroi(self):
        return 8


b1 = Bank()
b2 = SBI()
b3 = ICICI()
print("Bank Rate of interest:", b1.getroi())
print("SBI Rate of interest:", b2.getroi())
print("ICICI Rate of interest:", b3.getroi())


###########################################################################################

# Python Operator Overloading

# In Python, we can change the way operators work for user-defined types. For example, the + operator will perform
# arithmetic addition on two numbers, merge two lists, or concatenate two strings. This feature in Python that allows
# the same operator to have different meaning, according to the context, is called operator overloading.

# Python Special Functions:
# Class functions that begin with double underscore __ are called special functions in Python.
# They are called "double underscore" functions because they have a double underscore prefix and suffix,
# such as __init__() or __add__().

# Here are some of the special functions available in Python,

# Function --> Description
# __init__() --> initialize the attributes of the object
# __str__() --> returns a string representation of the object
# __len__() --> returns the length of the object
# __add__() --> adds two objects
# __call__() --> call objects of the class like a normal function

# -----------------------------------------------------------------------------------------

# Example: + Operator Overloading in Python

# To overload the + operator, we will need to implement __add__() function in the class.
# With great power comes great responsibility. We can do whatever we like inside this function.
# But it is more sensible to return the Point object of the coordinate sum.

# Let's see an example,

class Number:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __str__(self):
        return "addition of numbers using addition of objects = {0},{1}".format(self.a, self.b)

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Number(a, b)


num1 = Number(1, 1)  # obj 1
num2 = Number(2, 2)  # obj 2
print(num1 + num2)  # addition of objects

# In the above example, what actually happens is that, when we use num1 + num2,
# Python calls num1.__add__(num2) which in turn is Point.__add__(num1,num2).
# After this, the addition operation is carried out the way we specified.

num3 = Number(2, 2)  # obj 3
print(num1 + num2 + num3)  # addition of objects


# Similarly, we can overload other operators as well.

# Operator --> Expression --> Internally
# Addition --> num1 + num2 --> num1.__add__(num2)
# Subtraction --> num1 - num2 --> num1.__sub__(num2)
# Multiplication --> num1 * num2 --> num1.__mul__(num2)
# Power --> num1 ** num2 --> num1.__pow__(num2)
# Division --> num1 / num2 --> num1.__truediv__(num2)
# Floor Division --> num1 // num2 --> num1.__floordiv__(num2)
# Remainder (modulo) --> num1 % num2 --> num1.__mod__(num2)
# Bitwise Left Shift --> num1 << num2 --> num1.__lshift__(num2)
# Bitwise Right --> Shift num1 >> num2 --> num1.__rshift__(num2)
# Bitwise AND --> num1 & num2  --> num1.__and__(num2)
# Bitwise OR --> num1 | num2 --> num1.__or__(num2)
# Bitwise XOR --> num1 ^ num2 --> num1.__xor__(num2)
# Bitwise NOT  --> ~num1  --> num1.__invert__()


class Multiplication:
    def __init__(self, n1):
        self.n1 = n1

    def __mul__(self, other):
        n1 = self.n1 * other.n1
        return (n1)


a = Multiplication(2)
b = Multiplication(2)

print("multiplication of two objects =", a * b)


# -----------------------------------------------------------------------------------------

# Overloading Comparison Operators
# Python does not limit operator overloading to arithmetic operators only.
# We can overload comparison operators as well.

# Here's an example of how we can overload the < operator to compare two objects
# the Person class based on their age:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # overload < operator
    def __lt__(self, other):
        return self.age < other.age


p1 = Person("Alice", 5)
p2 = Person("Bob", 10)

print(p1 < p2)  # prints True
print(p2 < p1)  # prints False

# Here, __lt__() overloads the < operator to compare the age attribute of two objects.
# The __lt__() method returns,
#     True - if the first object's age is less than the second object's age
#     False - if the first object's age is greater than the second object's age

p3 = Person("Avi", 30)
print(p3 > p1)  # prints True


# Similarly, the special functions that we need to implement,
# to overload other comparison operators

# Operator --> Expression  --> Internally

# Less than --> p1 < p2  --> p1.__lt__(p2)
# Less than or equal to  --> p1 <= p2  --> p1.__le__(p2)
# Equal to --> p1 == p2 --> p1.__eq__(p2)
# Not equal to  --> p1 != p2 --> p1.__ne__(p2)
# Greater than --> p1 > p2 --> p1.__gt__(p2)
# Greater than or equal to --> p1 >= p2 --> p1.__ge__(p2)

###########################################################################################

# Note: Method Overloading, a way to create multiple methods with the same name but different arguments
# is not possible in Python directly.
# Python doesn't support method overloading on the basis of different number of parameters in functions.

###########################################################################################

# Method overloading:
# class have multiple methods with the same name with different arguments(method signature),
# or writing the same method with different args.
# ex:add(a), add(a,b) , add (a,b,c)
# this is not allowed in Python.

# -----------------------------------------------------------------------------------------
# Method overloading in python:
# we can achieve this using default arguments in python.

# ex:
class M:
    def display(self, a=None, b=None):  # default value = None
        print(a, b)


m1 = M()
m1.display()  # None,None
m1.display(1, 2)
m1.display("Hello", "World")


# -----------------------------------------------------------------------------------------
# ex:
class Mo:

    def add(self, a=0, b=0, c=0):  # default value = 0
        self.a = a
        self.b = b
        self.c = c
        return self.a + self.b + self.c


m1 = Mo()
print(m1.add())
print(m1.add(1))
print(m1.add(1, 2))
print(m1.add(0, 2, 3))


# -----------------------------------------------------------------------------------------
# Ex:
class Compute:
    # area method
    def area(self, x=None, y=None):
        if x is not None and y is not None:
            return x * y
        elif x is not None:
            return x * x
        else:
            return 0


# object
obj = Compute()
# zero argument
print("Area Value:", obj.area())
# one argument
print("Area Value:", obj.area(4))
# two argument
print("Area Value:", obj.area(3, 5))

###########################################################################################

# Note: Overriding will always happen in different class.

# overloading will happen in the same class

###########################################################################################