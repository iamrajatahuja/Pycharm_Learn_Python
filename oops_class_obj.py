# creating classes -blueprints,templates

class MyClass:
    """
    This is the class MyClass
    """
    pass

# creating objects  -instances of class contains attributes(data) and behavior(methods)

obj1 = MyClass()
obj2 = MyClass()

print(type(obj1))   #__main__ is Dunder, tells that class and objects are in same file

obj1.age = 10
print(obj1.age)
# print(obj2.age) //gives attribute error as no attributes defined in the class


# Docstring - __doc__
print(MyClass.__doc__)
print(help(MyClass))

print(obj1.__dict__) #gives the dictionary of attributes / variables associated with object
print(obj2.__dict__)
#########################################

#Instance methods - defined in the class which are associated with instance/object
l1=[1,2,3]
print(type(l1)) #l1 is the object of list class
print(help(list))
l1.append(4)   #append is instance method can be accessed via . dot notation
print(l1)

############################
class Student:
    def study(self):
        print(f"self is {self}")
        print("study")

student1 = Student()
print(f"The object is {student1}")
student1.study()
#When we call an instance method using the object of class,Python passes
#the object itself as the first argument to that method
#The first argument is by standard is self

###############################################33
class Student:
    def __init__(self):
        print("initializing the attributes of object")

student1 = Student()

#################################################
class Student:

    college_name = "ABC college"
    department_name = ["Arts","Science","Engineering"]

    def __init__(self,age):
        print(f"initializing the attributes {age}..college is {self.college_name}")
        self.age = age  #instance variables are defined inside __init__ method
                        # and every object has its own instance variables

student2 = Student(50)
print(student2.age)
print(student2.__dict__)

#Class variables - same copy shared with all the objects
help(Student)

print(Student.department_name)
print(student2.college_name,student2.department_name)

# class methods - are bound to the class and defined using decorator -> @classmethod

class Welcome:

    stu_name = "Hello"
    @classmethod
    def greet(cls):
        print(cls)
        print(f"{cls.stu_name} Welcome to OOPS")
        for stu in cls.stu_name:
            print(stu)

w1 = Welcome()
w1.greet()

#static method - neither bound to class or object. to create we use decorator @staticmethod
class Welcome2:

    @staticmethod
    def greet():
        print("Welcome to OOPS")

w2 = Welcome2()
w2.greet()

#Inheritance syntax
#Welcome3 child/derived class and Welcome2 base/parent class
# when 1 class is inherited from 1 class is called single inheritance
class Welcome3(Welcome2):
    pass
#w3 = Welcome3()
# w3 is the object of both the classes child and parent
# w3 will use __init__ method in child class , if not present taking the __init__ of parent class

help(Welcome3)
###########################

#We have to explicitly call the __init__ method of parent class in child class __init__ method
class Welcome4(Student):
    def __init__(self,name):
        print("init of welcome4")
        self.name = name
        super().__init__(19) #no need to pass self
#or this way ->   Student.__init__(self,18)

w4=Welcome4("Bob")
print(w4.age)
print(w4.__dict__)

#################
#Multiple inheritance syntax - class A(B,C):
#Multilevel inheritance -
# class A
# class B(A)
# class C(B)

####################################
# Polymorphism - characteristic of an entity to present in more than one form

#Operator overloading
help(int)

a=2
b=9
#Internally dunder method __add__ is called for +
print(a+b) #a.__add__(b) => int.__add__(a,b)

a="Hello"
b="World"
print(a+b) #str.__add__(a,b)

class A:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def f1(self, val):
        pass
    def __add__(self, other):
        return self.length + other.length
obj1=A(2,3)
obj2=A(4,5)
#obj.f1(20) #A.f1(obj,20)
print(obj1+obj2) # + will call A class __add__ method => A.__add__(obj1+obj2)

#############
# Python doesn't support method overloading the updated method will get execute

class B:
    def subt(self,num1,num2):
        return num1-num2
    def subt(self,num1,num2,num3):
        return num1-num2-num3
obj = B()
#print(obj.subt(5,6)) gives error argument missing
print(obj.subt(2,3,1))

#Method overriding - if there is same method in base and child class ,
# the child class method gets executed for child object and parent class method
# execute with parent class object

class Employee:
    def work_hrs(self):
        return 45
class Intern(Employee):
    def work_hrs(self):
        return 60

i= Intern()
print(i.work_hrs())
j= Employee()
print(j.work_hrs())

################################################
# Abstract class has 1 or more abstract methods which needs to be implemented by child classes otherwise no object is created
# we have abs module from which we have ABS(abstract class) and decorator @abstractmethod

from abc import ABC,abstractmethod

class Z(ABC):
    @abstractmethod
    def area(self):
        pass
