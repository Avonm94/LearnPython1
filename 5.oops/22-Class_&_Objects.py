# Python Class, Object & Method.
###########################################################################################
# Class:
# The class can be defined as a collection of objects.
# It is a logical entity that has some specific attributes and methods.
# For example, if you have an employee class, then it should contain an attribute and method,
# i.e., an email id, name, age, salary, etc.

# A class is a blueprint or a template for creating objects while an object is an instance
# or a copy of the class with actual values.

# Note: The variables inside a class are called attributes.
# Attributes are Variables and behaviors are methods of the class.

# Creating a Class:
# Create a class using the class keyword.
# Ex1:
class Pets:
    # class attribute
    type = ""
    color = ""
    age = 0


# Ex2:
class Form:
    # class attribute
    name = ""
    age = 0
    gender = ''


# Ex3:
class Bike:
    name = ""
    gear = 0


# Here,
# Bike - the name of the class
# name/gear - variables inside the class with default values "" and 0 respectively.

###########################################################################################

# Object:
# The object is an entity that has state(attributes) and behavior.
# It may be any real-world entities like the mouse, keyboard, chair, table, pen, etc.

# Attributes:
# Name, class, subjects, marks, etc., of student
# Name, designation, department, salary, etc., of employee
# Invoice number, customer, product code and name, price and quantity, etc., in an invoice
# Registration number, owner, company, brand, horsepower, speed, etc., of car
# Each attribute will have a value associated with it. Attribute is equivalent to data.

# Behavior:
# Processing attributes associated with an object.
# Compute percentage of student's marks
# Calculate incentives payable to employee
# Apply GST to invoice value
# Measure speed of a car
# Behavior is equivalent to function. In real life, attributes and behavior are not independent of each other,
# rather they co-exist.

# An object is any entity that has attributes and behaviors. For example, a Pet is a class, a dog is an object. It has
# attributes - name, age, gender, etc.
# behavior - dancing, singing, etc.

# Access Class Attributes Using Objects
# We use the . notation to access the attributes of a class.

# Creating an Object:
# Ex1:
# Pets object1
pets1 = Pets()
pets1.type = "Dog"
pets1.age = 3
pets1.color = "Black"

# Pets object2
pets2 = Pets()
pets2.type = "Cat"
pets2.age = 2
pets2.color = "White"

# access attributes
print(f"{pets1.color} {pets1.type} is {pets1.age} years old")
print(f"{pets2.color} {pets2.type} is {pets2.age} years old")

# Ex2:
# Form object1
form1 = Form()
form1.name = "Avinash"
form1.age = 29
form1.gender = "Male"

# Form object1
form2 = Form()
form2.name = "Priya"
form2.age = 25
form2.gender = "Female"

# access attributes
print(f"{form1.name} is {form1.age} old {form1.gender}")
print(f"{form2.name} is {form2.age} old {form2.gender}")


# Ex3:
# create class
class Bike:
    name = ""
    gear = 0


# create objects of class
bike1 = Bike()
bike1.name = "Mountain Bike"
bike1.gear = 12


# Here, we have used bike1.name and bike1.gear to change
# and access the value of name and gear attribute respectively.

# -----------------------------------------------------------------------------------------

# Example:
# define a class
class Bike:
    name = ""
    gear = 0


# create an object of class
bike1 = Bike()

# access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")


# In the above example, we have defined the class named Bike with two attributes: name and gear.
# We have also created an object bike1 of the class Bike.
# Finally, we have accessed and modified the attributes of an object using the . notation.


# Ex: Create Multiple Objects of Python Class
# We can also create multiple objects from a single class. For example,
# define a class
class Employee:
    # define an attribute
    employee_id = 0


# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()

# access attributes using employee1
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

# access attributes using employee2
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")


###########################################################################################

# Method
# The method is a function associated with an object.
# A Python Function defined inside a class is called a method.
# In Python, a method is not unique to class instances. Any object type can have methods.
# A method with self as one of the formal arguments is called instance method, as it is called by a specific object.

# Note:
# In python methods and functions are the same.
# Functions are created without class.
# Methods are created inside class.

# -----------------------------------------------------------------------------------------

# Self method
# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.
# It must be provided as the extra parameter inside the method definition.

# Example:
class Details:  # Class
    name = "Simran"
    age = 20

    def intro(self):  # method
        print("My name is", self.name, "and I'm", self.age, "years old.")


obj1 = Details()  # created an object for the class
obj1.intro()  # called the method from the class


# whenever you are a creating function/method inside the class, it should have self keyword as an args.
# self keyword indicates that the created method belongs to that particular class.


class family:
    surname = ''
    members = 0

    def intro(self):
        print("Surname: ", self.surname, " Total Members: ", self.members)


fam1 = family()
fam1.surname = "Malage"
fam1.members = 4
fam1.intro()


# ex:
# create a class
class Room:
    length = 0.0
    breadth = 0.0

    # method to calculate area
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)


# create object of Room class
study_room = Room()

# assign values to all the attributes
study_room.length = 42.5
study_room.breadth = 30.8

# access method inside class
study_room.calculate_area()


# In the above example, we have created a class named Room with:
# Attributes: length and breadth
# Method: calculate_area()
# Here, we have created an object named study_room from the Room class.
# We then used the object to assign values to attributes: length and breadth.
# Notice that we have also used the object to call the method inside the class,
# study_room.calculate_area()
# Here, we have used the . notation to call the method.
# Finally, the statement inside the method is executed.

# -----------------------------------------------------------------------------------------

# __init__ constructor:
# In Python, the method the __init__() simulates the constructor of the class.
# It accepts the self-keyword as a first argument which allows accessing the attributes or method of the class.
# The __init__ constructor is used to initialize the object’s state and contains 3.statements that
# are executed at the time of object creation.

# Ex: Default constructor (not having parameter or args.)
class Myclass:
    def __init__(self):
        print("this is a constructor")

    def m1(self):
        print("this is method")


mc1 = Myclass()  # this will invoke the constructor and print "this is a constructor"
mc1.m1()  # here we are calling method explicitly.


# Ex1: parameterized constructor (accepts parameter or args.)
class Pokemon:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        print(self.name, "belongs to the", self.group, "group.")


obj1 = Pokemon("Pikachu", "Electrical")
obj2 = Pokemon("Charizard", "Fire")


# Ex2:
class Bike:

    # constructor function
    def __init__(self, name=""):
        self.name = name


bike1 = Bike("mountain bike")
bike2 = Bike("dirt bike")

print(bike1.name)
print(bike2.name)


# note: self-keyword is to use to access variable anywhere inside the class.


# Here, __init__() is the constructor/function/menthod that is called whenever
# a new object of that class is instantiated.

# The constructor above initializes the value of the name attribute.
# We have used the self.name to refer to the name attribute of the bike1 object.

# If we use a constructor to initialize values inside a class,
# we need to pass the corresponding value during the object creation of the class.
# bike1 = Bike("Mountain Bike")
# Here, "Mountain Bike" is passed to the name parameter of __init__().

# method vs constructor
# in pythod we can give any name to method, but not to __init--(self)
# method will return the value and __init()__ constructor will not return.
# method we have to invoke by using 'objectname.methodname()',
# __init()__ will be invoked at the time of object creation.

# Ex:Counting the number of objects of a class
# The constructor is called automatically when we create the object of the class. Consider the following example.
# Example
class Student:
    count = 0

    def __init__(self):
        Student.count = Student.count + 1


s1 = Student()
s2 = Student()
s3 = Student()
print("The number of students:", Student.count)

# Note: The constructor overloading is not allowed in Python.

###########################################################################################

# Variables
# Global Variable
# Local Variable
# Class Variable

x = 10  # global variable
print(x, " this is global variable")


class Num:
    a = 20  # class variable
    print(a, " this is class variable")

    def m1(self):
        b = 30  # local variable
        print(x, " this is global variable accessed inside method")
        print(self.a, " this is class variable accessed inside method")
        print(b, " this is local variable accessed inside method")


num1 = Num()
num1.m1()


class MyClass:
    print(Num.a, " this is class variable accessed in different class")


###########################################################################################

# example:

class Emp:
    def __init__(self, name, empid):
        self.name = name
        self.empid = empid

    def p(self):
        print(f"Employee {self.name} is having {self.empid} employee id")


emp1 = Emp("Avi", 100)
emp1.p()
emp2 = Emp("Aru", 101)
emp2.p()


# there is __str__ constructor which will returns string.

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        print("this is __str__() which only return string data.")
        return self.name

    def dis(self):
        print(f"Student {self.name} is having {self.id} id")


s1 = Student(11, 'Avi')
s1.dis()
print(s1)  # __str__() invoked and printed returned value


###########################################################################################

# Python built-in class functions

# Function --> Description
# getattr(obj,name,default) --> It is used to access the attribute of the object.
# setattr(obj, name,value) --> It is used to set a particular value to the specific attribute of an object.
# delattr(obj, name) --> It is used to delete a specific attribute.
# hasattr(obj, name) --> It returns true if the object contains some specific attribute.

# Example

class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age


# creates the object of the class Student
s = Student("John", 101, 22)

# prints the attribute name of the object s
print(getattr(s, 'name'))

# reset the value of attribute age to 23
setattr(s, "age", 23)

# prints the modified value of age
print(getattr(s, 'age'))

# prints true if the student contains the attribute with name id
print(hasattr(s, 'id'))

# deletes the attribute age
delattr(s, 'age')

# this will give an error since the attribute age has been deleted
# print(s.age)

###########################################################################################

# Built-in class attributes

# Along with the other attributes, a Python class also contains some built-in class
# attributes which provide information about the class.

# Attribute --> Description
# __dict__ --> It provides the dictionary containing the information about the class namespace.
# __doc__ --> It contains a string which has the class documentation
# __name__ --> It is used to access the class name.
# __module__ --> It is used to access the module in which, this class is defined.
# __bases__ --> It contains a tuple including all base classes.

# Example
class Student:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
    def display_details(self):
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))

s = Student("John",101,22)
print(s.__doc__)
print(s.__dict__)
print(s.__module__)

###########################################################################################
# reference
# https://www.tutorialspoint.com/python
# https://www.javatpoint.com/
# https://www.w3schools.com/python
# https://www.programiz.com/python-programming

###########################################################################################