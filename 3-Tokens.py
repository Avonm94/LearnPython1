# Tokens:
# The tokens can be defined as a punctuator mark, reserved words, and each word in a statement.
# The token is the smallest unit inside the given program.

# There are the following tokens in Python:
# Keywords.
# Identifiers.
# Literals.
# Operators.
###########################################################################################

# Python Variables
# A variable is the name given to a memory location.
# A value-holding Python variable is also known as an identifier.
# Since Python is an infer language that is smart enough to determine the type of variable,
# we do not need to specify its type in Python.
# Variable names must begin with a letter or an underscore, but they can be a group of both letters and digits.

# The name of the variable should be written in lowercase. Both avinash and Avinash are distinct variables.

# Identifier Naming
# Identifiers are things like variables. An Identifier is utilized to recognize the literals utilized in the program.
# The standards to name an identifier are given underneath.
# The variable's first character must be an underscore or alphabet (_).
# Every one of the characters with the exception of the main person might be a letter set of lower-case(a-z),
# capitalized (A-Z), highlight, or digit (0-9).
# White space and special characters (!, @, #, %, etc.) are not allowed in the identifier name. ^, &, *).
# Identifier name should not be like any watchword characterized in the language.
# Names of identifiers are case-sensitive; for instance, my name, and MyName isn't something very similar.
# Examples of valid identifiers: a123, _n, n_9, etc.
# Examples of invalid identifiers: 1a, n%4, n 9, etc.

###########################################################################################
# Identifier Naming Best Practices:
# Names should describe the entity's purpose or content. Try "num_students"
# instead of "x".
# Use consistent naming. Snake_case variables and functions. Classes utilize
# CamelCase.
# Avoid single-character or cryptic abbreviations. Choose self-explanatory names to
# improve code readability.
# Avoid name conflicts with existing variables and functions by considering the
# context and scope of your identifiers.
# Valid, useful IDs include:
# Variable identifier
age = 25
# Function identifier
def calculate_area(length, width):
    return length * width

# Class identifier
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
# Module identifier
import math
# Constant identifier (common convention: all uppercase)
PI = 3.14

###########################################################################################



