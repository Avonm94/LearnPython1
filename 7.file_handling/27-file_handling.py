# Python File Handling
###########################################################################################
# File handling in python lets you open, read, write, append, modify files.

# Before we perform any operation on file, we need to open the file. This is done using the open() function.

# Example: lets say we have a text file (someText.txt) with some content in it.
# The open() function creates a file object with read() method for reading the content.

# if file is present in the same folder or directory
file = open("someText.txt")
print(file.read())

# if the file is present in different directory, then we have to pass a path of the file with fwd slashes.
file = open("C:/Users/malag/PycharmProjects/LearnPython/test.txt")
print(file.read())
# -----------------------------------------------------------------------------------------

# There are various modes in which we can open files.
# read (r): This mode opens the file for reading only and gives an error if the file does not exist.
# This is the default mode if no mode is passed as a parameter.
# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
# create (x): This mode creates a file and gives an error if the file already exists.

###########################################################################################

# Read/Write Files:

# A.Create a File:
# Creating a file is primarily done using the create (x) mode.
# Example:

# file = open("Text.txt", "x")

# Output:
# A file named Text.txt is created with no content.

# -----------------------------------------------------------------------------------------

# B.Write onto a File:
# This method writes content onto a file.

# Example:
file = open("Text.txt", "w")  # opening file for writing mode

file.write("This line is written through python code.\n")  # writing data
file.write("line 1.\n")
file.write("line 2.\n")

file.close  # closing the file

# -----------------------------------------------------------------------------------------

# C.Read a File:
# This method allows us to read the contents of the file.

# Example:
# file = open("Text.txt", "r")
# print(file.read())


file = open("Text.txt")
print(file.read())  # opening file in reading mode.
# print(file.readline()) # this will print/read only the first line.

file.close

# -----------------------------------------------------------------------------------------

# D. Append a File
# This method appends content into a file.

# Example:
file = open("Text.txt", "a")
file.write("This is an example of file appending.\n")
file.write("This is an example of file appending.\n")
file.close

file = open("Text.txt")
print(file.read())
file.close

###########################################################################################