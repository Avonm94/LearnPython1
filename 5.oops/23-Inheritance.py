# Python Inheritance
# acquiring all attributes (variables) and behaviours (methods) from one class to another class is called
# inheritance.
###########################################################################################
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Ex:
# class A -->  a,b,c  m1(), m2() --> A is Parent/Base/Super class.
# class B(A) --> x,y,z m3() --> B is Child/Sub/Derived class of A.
# b = B(), --> x,y,z,a,b,c m3(),m1(),m2().

# In above ex, Class A is having variable: a,b,c & method: m1(), m2()
# Class B is having variable: x,y,z & method: m3(),
# Class B is derived from Class A, so it is inherited all the variables and method of Class A.
# So, when we create and object b for Class B we can access all the variables,methods of Class B as well as Class A.


# Python Inheritance Syntax
# Here's the syntax of the inheritance in Python,
# define a superclass
# class Super_class:
# attributes and method definition

# inheritance
# class Sub_class(Super_class):
# attributes and method of super_class
# attributes and method of sub_class

# Here, we are deriving the Sub_class class from the Super_class class.

# -----------------------------------------------------------------------------------------

# is-a relationship

# In Python, inheritance is an is-a relationship. That is, we use inheritance only
# if there exists an is-a relationship between two classes. For example,
# a Car is a Vehicle,
# Apple is a Fruit
# Cat is an Animal
# Here, Car can inherit from Vehicle, Apple can inherit from Fruit, and so on.

###########################################################################################

# Types of Inheritance in python:

# Single Inheritance --> 1 parent & 1 child
# Ex: A --> B
# Class A is parent, Class B is a child of A

# Example:
s = 'Single Inheritance'
print(s.center(50, "-"))


# Parent class representing a generic animal
class Animal:
    def eat(self):
        print("Animal will eat")


# Child class Dog inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Dogs will bark..Woof!")


# Usage
my_dog = Dog()
my_dog.eat()  # Inherited from Animal
my_dog.bark()  # Specific to Dog

# Here, the Dog class inherits from the Animal class.
# This means that Dog objects can access and use all the methods and attributes of Animal objects.
# Additionally, Dog objects can have their own methods and attributes,
# such as the bark() method in this example.

# -----------------------------------------------------------------------------------------

# Multi-Level Inheritance --> 1 parent & 1 child & child will have its own child...
# Ex: A --> B --> C --> D ...
# Class A is parent, Class B is a child of A and Class C is a child of Class B

s = 'Multi-Level Inheritance'
print(s.center(50, "-"))


# Parent class representing a generic animal
class Animal:
    def eat(self):
        print("Animal will eat")


# Class representing a Mammal, inheriting from Animal
class Mammal(Animal):
    def breathe(self):
        print("Some animals are Mammals they breath")


# Child class Dog inheriting from Mammal
class Dog(Mammal):
    def bark(self):
        print("Dogs will bark..Woof!")


# Usage
my_dog = Dog()
my_dog.eat()  # Inherited from Animal
my_dog.breathe()  # Inherited from Mammal
my_dog.bark()  # Specific to Dog

# Here, the Dog class inherits from the Mammal class, which in turn inherits from the Animal class.
# This means that Dog objects can access and use all the methods and attributes of both Animal and Mammal objects.

# -----------------------------------------------------------------------------------------

# Multiple Inheritance --> Multiple(2) Parent & 1 Child
# Ex: A,B --> C
# Class A and B are a parent class of Class C, whereas class C will have properties of both A & B.

s = 'Multiple Inheritance'
print(s.center(50, "-"))


class Animal:
    def eat(self):
        print("Animal will eat")


class Mammal:
    def breathe(self):
        print("Some animals are Mammals they breath")


class Dog(Animal, Mammal):
    def bark(self):
        print("Dogs will bark..Woof!")


my_dog = Dog()
my_dog.eat()  # Inherited from Animal
my_dog.breathe()  # Inherited from Mammal
my_dog.bark()  # Specific to Dog

# In this example, the Dog class inherits from both the Animal and Mammal classes.
# This means that Dog objects can access and use all the methods and attributes of both Animal and Mammal objects.

# -----------------------------------------------------------------------------------------

# Hierarchy Inheritance --> 1 parent & multiple children
# Ex: A --> B, A --> C, A --> D
# Class A is parent, Class B, C, D are children of Class A, these children are not inheriting each other.

s = 'Hierarchy Inheritance'
print(s.center(50, "-"))


class Animal:
    def eat(self):
        print("Animal will eat")


class Mammal(Animal):
    def breathe(self):
        print("Some animals are Mammals they breath")


class Dog(Mammal):
    def bark(self):
        print("Dogs will bark..Woof!")


class Cat(Mammal):
    def meow(self):
        print("Cats will mewo..Meow!")


my_dog = Dog()
my_dog.eat()  # Inherited from Animal
my_dog.breathe()  # Inherited from Mammal
my_dog.bark()  # Specific to Dog

my_cat = Cat()
my_cat.eat()  # Inherited from Animal
my_cat.breathe()  # Inherited from Mammal
my_cat.meow()  # Specific to Cat


# Here, both the Dog and Cat classes inherit from the Mammal class,
# which in turn inherits from the Animal class.
# This creates a hierarchy of classes where Animal is the base class,
# Mammal is the intermediate class, and Dog and Cat are the leaf classes.

# -----------------------------------------------------------------------------------------

# Ex1:
class Hero:
    def power(self):
        print("Rich")


class Ironman(Hero):
    def speciality(self):
        print("Genius", "Millionaire", "Playboy", "Philanthropist")


obj = Ironman()
obj.power()
obj.speciality()


# The class Hero has a method power that returns a specific power a hero has.
# Then we created a subclass Ironman that inherits the superclass Hero, and
# the subclass Ironman has its own method speciality that specifies the specialties of Ironman.
# The subclass Ironman now has access to all the attributes and methods of the superclass Hero as well.
# We accessed the method power using the class Ironman which inherited the method power from the class Hero.

# -----------------------------------------------------------------------------------------

# Ex:
# Base class
class Hero:
    # Constructor function
    def __init__(self, reel_name, hero_name):
        self.reel_name = reel_name
        self.hero_name = hero_name

    def show(self):
        print(self.reel_name)
        print(self.hero_name)


# Derived class
class Name(Hero):
    def __init__(self, real_name, reel_name, hero_name):
        self.real_name = real_name
        # Calling the __init__ of the parent class
        Hero.__init__(self, reel_name, hero_name)

    def display(self):
        print(self.real_name)
        Hero.show(self)


obj = Name("RDJ", "Tony Stark", "IronMan")
obj.display()
print("-" * 20)
obj.show()


# In the above code, we created the base class Hero and inside it,
# we defined the constructor function that takes two arguments reel_name and
# hero_name, and then we defined the function show that prints the reel_name and hero_name.
# Then we created a subclass Name that inherits the superclass Hero and
# then we created a constructor function that takes three arguments real_name, reel_name, and hero_name.
# To access the objects of the parent class Hero,
# we invoked __init__ of the parent class Hero and passed the required arguments.
# Next, we created a function display that prints the real_name and
# calls the function show from the class Hero.
# Then we created obj an instance of the class Name and called the function display and show.

# -----------------------------------------------------------------------------------------

# Ex:
# Base Class
class GrandPa:
    def __init__(self):
        self.age = 100


# Derived CLass
class Parent(GrandPa):
    def __init__(self):
        self.name = "Geek"
        GrandPa.__init__(self)


# Derived Class
class GrandChild(Parent):
    def __init__(self):
        self.hobby = "Gaming"
        Parent.__init__(self)

    def display(self):
        print("Grandpa:", self.age)
        print("Parent:", self.name)
        print("Grandchild:", self.hobby)


obj = GrandChild()
obj.display()


# In the above code, the subclass Parent inherits from the superclass GrandPa and
# now the first subclass Parent has access to the methods of the superclass GrandPa.
# Then another subclass GrandChild inherited from the first subclass Parent
# and it has access to the methods that both the first subclass and superclass have.

###########################################################################################

# Hybrid Inheritance
# This type of inheritance is a blend of different inheritance which means it has a combination of
# two different types of inheritance like multiple or multi-level inheritances or multiple or single inheritances.
# Here is an example showing the demonstration of hybrid inheritance.

# Ex:
# Base Class
class Role:
    def role(self):
        print("Protagonist")


# Derived Class
class Luffy(Role):
    def power(self):
        print("Gum-Gum devil fruit")


# Derived Class
class Naruto(Role):
    def power1(self):
        print("Nine-tail fox")


# Derived Class
class Anime(Luffy, Naruto):
    def anime(self):
        print("They are anime characters.")


obj = Anime()
obj.role()
obj.power()
print("-" * 20)
obj.role()
obj.power1()
print("-" * 20)
obj.anime()

print("-" * 20)


# In the above code, the subclasses Luffy and Naruto inherit from the superclass Role
# and then the subclass Anime inherits from the subclasses Luffy and Naruto.
# The first scenario where Luffy and Naruto inherit from the superclass Role
# shows the single inheritance and the second scenario where Anime inherits
# from the subclasses Luffy and Naruto shows the multiple inheritances.

# https://geekpython.in

###########################################################################################

# Method Overriding
# We can provide some specific implementation of the parent class method in our child class.
# When the parent class method is defined in the child class with some specific implementation,
# then the concept is called method overriding.

# Ex 1:
class Animal:
    def voice(self):
        print("Animal:Voice")


class Dog(Animal):
    def voice(self):
        print("Dog:Barks")


class Cat(Animal):
    def voice(self):
        print("Cat:Meows")


class Lion(Animal):
    def voice(self):
        print("Lion:Roars")


any_animal = Animal()
any_animal.voice()

my_dog = Dog()
my_dog.voice()

my_cat = Cat()
my_cat.voice()

my_lion = Lion()
my_lion.voice()


# -----------------------------------------------------------------------------------------

# Ex2:

class Vehical:
    def specs(self, name, speed):
        self.name = "name"
        self.speed = "speed"
        print(f"{name}:{speed}/km")


class Car(Vehical):
    def specs(self, name, speed):
        self.name = "name"
        self.speed = "speed"
        print(f"{name}:{speed}/km")


class Bike(Vehical):
    def specs(self, name, speed):
        self.name = "name"
        self.speed = "speed"
        print(f"{name}:{speed}/km")


car1 = Car()
car1.specs('Supra', 300)

car2 = Car()
car2.specs('Mustang', 320)

bike1 = Bike()
bike1.specs('Hayabusa', 300)

bike2 = Bike()
bike2.specs('Kawasaki', 350)


# -----------------------------------------------------------------------------------------
class Animal:
    # attributes and method of the parent class
    name = ""

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # override eat() method
    def eat(self):
        print("I like to eat bones")


# create an object of the subclass
labrador = Dog()

# call the eat() method on the labrador object
labrador.eat()


# In the above example, the same method eat() is present in both the Dog class and the Animal class.
# Now, when we call the eat() method using the object of the Dog subclass, the method of the Dog class is called.
# This is because the eat() method of the Dog subclass overrides the same method of the Animal superclass.

# -----------------------------------------------------------------------------------------

# Ex:
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


# -----------------------------------------------------------------------------------------

# The super() Method in Python Inheritance:
# if we need to access the superclass method from the subclass, we use the super() method

class A:
    def m1(self):
        print("this is m1 method from Class - A (parent class)")


class B(A):
    def m1(self):
        print("this is m1 method from Class - B (child class) ( m1 is overridden in Class - B)")
        super().m1()  # this will invoke parent class method through child class method.


b = B()
b.m1()


# -----------------------------------------------------------------------------------------

# Ex:
class Animal:
    name = ""

    def breath(self):
        print("Breath")

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    def breath(self):
        super().breath()
        print("I breath oxygen")

    # override eat() method
    def eat(self):
        # call the eat() method of the superclass using super()
        super().eat()

        print("I like to eat bones")


# create an object of the subclass
lab = Dog()
lab.breath()
lab.eat()


###########################################################################################

# override variables:

class Parent:
    name = 'Thomas Wayne'


class Child(Parent):
    name = 'Bruce Wayne'  # overridng the parent value later will print

    def papa(self):
        print(super().name) # accessing parent value and printing


child1 = Child()
print(child1.name)
child1.papa()
###########################################################################################

# Note: Overriding will always happen in different class.

# overloading will happen in the same class

###########################################################################################