# Python Packages
###########################################################################################
# Python packages are essentially folders that contain many python modules.
# As such, packages help us to import modules from different folders.

# Here are some packages provided by python,
# NumPy, SciPy, Pandas, Seaborn, sklearn, Matplotlib, etc.

# -----------------------------------------------------------------------------------------
# Python PIP
# pip stands for Package Installer for Python.
# It  is used to install and manage software packages in python that are not the part of standard python library.
# In the later versions of python (3.4 and after), the pip command is pre-installed.
# To Check if pip is installed in your system, type the following in command prompt:
# pip --version
# -----------------------------------------------------------------------------------------
# If your system does not have pip installed, you can easily download it from their official website: https://pypi.org/project/pip/
# Now that pip has been installed in our system, we can download packages in system.
# pip list
# -----------------------------------------------------------------------------------------
# PyCharm provides methods for installing, uninstalling, and upgrading Python packages for a particular Python interpreter.
# It means that each project has its own set of packages,
# which is considered a best practice for Python dependency management.
# By default, PyCharm uses pip to manage project packages.

# In PyCharm, you can preview and manage packages in the Python Packages tool window and in the Python interpreter settings.
# https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html#upgrade-packages
# -----------------------------------------------------------------------------------------

# https://www.codewithharry.com/tutorial/python-pip/
# https://www.tutorialspoint.com/what-is-a-python-module-how-is-it-different-from-libraries


# A library is a collection of related modules or packages

###########################################################################################

# Python Package

# Package --> collections of modules
# package --> modules --> classes, functions & variables.

# A package is a container that contains various functions to perform specific tasks.
# For example, the math package includes the sqrt() function to perform the square root of a number.
# While working on big projects, we have to deal with a large amount of code,
# and writing everything together in the same file will make our code look messy.
# Instead, we can separate our code into multiple files by keeping the related code together in packages.

# -----------------------------------------------------------------------------------------

# importing module from the same package
# Ex: pack1 --> module1 --> display
#           --> module2 --> show
#  access this in client which is not part of pack1.

# -----------------------------------------------------------------------------------------

# importing module from two package (sub package)
# Ex: pack1 --> module1 --> display
#     pack1--> pack2 --> modulea --> show

# pack2 is subpackage in pack1
#  access these in client which is not part of the packages.
# -----------------------------------------------------------------------------------------

# importing module from two package
# package --> module --> class --> method
# packA --> emp --> Employee --> displayemp()
# packB --> stu --> STudent --> displaystu()

#  access these in client which is not part of the packages.
# -----------------------------------------------------------------------------------------

# create pack1 package: right-click on directory, create new python package.

# next goto client.py file.

# -----------------------------------------------------------------------------------------