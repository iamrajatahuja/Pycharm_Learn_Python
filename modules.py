# .py file is a module
#Built-in modules
#Syntax
# import module_name
# import module_name as alias_name
# from module_name import f1,f2.f3 or variable_name v1

from math import sqrt,pi
print(sqrt(5))
print(pi)

import datetime as dt
print(dt.time(4,5,30))
print(dt.date.today())


#User defined modules

# Just for understanding
# that value of __name__(Dunder variable) in user_defined_file is main but in modules.py file
# the value of __name__ is user_defined_modules that is why 5 is not getting printed
# dunder variable holds the value of current module

print(f"modules file: {__name__}")
from user_defined_modules import squareroot
print(f"modules file: {__name__}")
print(squareroot(100))