###########################################################################################
# Ex1
# -----------------------------------------------------------------------------------------
# Approach 1: using sys and path
# first import predefined sys package
import sys

# then we need to specify a path of pack1 as string using fwd slash
sys.path.append("C:/Users/malag/PycharmProjects/LearnPython/4.python_functions_modules_package/pack1")

# now import modules
import module1
import module2

module1.display()
module2.show()

print('-'*50)

# -----------------------------------------------------------------------------------------
# Approach 2 using from keyword

from module1 import *
from module2 import *

display()
show()

print('-'*50)
# -----------------------------------------------------------------------------------------
# Approach 3

import pack1.module1
import pack1.module2
display()
show()

print('-'*50)

###########################################################################################


# Ex2:

# Approach 1: using sys and path

import sys
sys.path.append("C:/Users/malag/PycharmProjects/LearnPython/4.python_functions_modules_package/pack1")
sys.path.append("C:/Users/malag/PycharmProjects/LearnPython/4.python_functions_modules_package/pack1/pack2")

import module1
import modulea

module1.display()
modulea.show()

print('-'*50)

# -----------------------------------------------------------------------------------------
# Approach 2 using from keyword

from module1 import *
from modulea import *

display()
show()

print('-'*50)

# -----------------------------------------------------------------------------------------
# Approach 3

import pack1.module1
import pack1.pack2.modulea
display()
show()

print('-'*50)

##########################################################################################

# Ex3:

# Approach 1: using sys and path

import sys
sys.path.append("C:/Users/malag/PycharmProjects/LearnPython/4.python_functions_modules_package/pack_A")
sys.path.append("C:/Users/malag/PycharmProjects/LearnPython/4.python_functions_modules_package/pack_B")

import emp
import stu
e1 = emp.Employee()
e1.displayemp()


s1 = stu.Student()
s1.displaystu()

print('-'*50)

# -----------------------------------------------------------------------------------------
# Approach 2
from emp import *
from stu import *

e2=Employee()
e2.displayemp()

s2=Student()
s2.displaystu()

print('-'*50)
# -----------------------------------------------------------------------------------------
# Approach 3
import pack_A.emp
import pack_B.stu

e3=Employee()
s3=Student()

e3.displayemp()
s3.displaystu()

print('-'*50)

##########################################################################################