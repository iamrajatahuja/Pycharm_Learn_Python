# 1 Compile time errors - Syntax and Indentation errors
# 2 Run time error(Exceptions) - errors during execution called Built-in Exceptions
# like NameError FileNotFoundError ZeroDivisionError...
# Exceptions are handled by try/except block

try:
    n1=int(input("enter a number"))
    n2=int(input("enter another number"))
    result = n1/n2
    print(result)

except ZeroDivisionError:
    print("division by zero")
except ValueError as e:
    print("enter only integer")
    print(e)
except Exception as x:
    print("Something went wrong") #if any other error occurs write Exception(which is child of BaseException) which is base class or all errors OR except: only
    print(x)
else:
    print("hello world") #else block runs if there is no error in try block
finally:
    print("Everytime") #finally executes irrespective of any error in try block

#Raising exception - changing text of error

age = int(input("enter your age"))
if age<0:
    raise ValueError("Your age is negative") # OR raise Exception("")
else:
    print("Your age is",age)


##########################3
# user defined exceptions

class SalaryError(Exception):
    pass
def get_salary(salary):
    if salary<0:
        raise SalaryError("Your salary is negative")
    else:
        print("Your salary is",salary)

salary = int(input("enter your salary"))
get_salary(salary)