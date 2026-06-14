#for loop can run with list,string,tuple,set,dictionary

e="Hello W"
for i in e:
    print(i)

emp={'eid':1001,'name':'Raj', 'age':25}

for i in emp:
    print(i)
    print(emp[i])

print(emp.items())
for i in emp.items():
    print(i)
    print(i[0],i[1])

# Range is built in function similar to slicing
# range(start,stop,step)
# range(start,stop) default step = 1
# range(stop) default start = 0 and step = 1

for x in range(1,11,2):
    print(x)
print("Reverse countdown")
for x in range(10,0,-1):
    print(x)


l1=[9,4,2,10]

for index in range(len(l1)):
    print(index, l1[index])

#star pattern
for i in range(1,5):
    for j in range(1,i+1):
        print('*',end='')
    print()

#while loop

n=1
while n<=10:
    print(n)
    n+=1

#Function returns None if not returning anything
def sum1(a,b=10,c=8):    #b and c has default value and they are in the end of argument list
    return a+b+c
print(sum1(1,2,3))
print(sum1(1,2))
print(sum1(19))
print(sum1(c=50,a=6)) #keyword arguments like c where position doesn't matter

#variable *args or any other *word -  (0 to n) arguments

def add(*args):
    print(args, type(args))
    print(sum(args))
add()
add(1,2,3,4)

# variable **kwargs - keyword arguments (0-n) and they should be in the end of argument list

def func(a,*num,**kwargs):
    print(a,num,kwargs, type(kwargs))
func(110,b=2,c=3)
func(3,5,5,7,b=0)

#Docstring in functions
# It should be the first thing to do in function definition """ """

def funct(a,b):
    """
    This function divides
    :param a: Numerator
    :param b: Denominator
    :return: float (if denominator not 0) or string (if denominator is 0)
    """
    if b==0:
        return "Divided by 0"
    else:
        return a/b

help(funct) #help function returns None
help(len)

#Global and local variable

g=4
def fn1():
    g=3
    print(g)
fn1()
print(g)

h=8
def fn2():
    global h      #to modify global h inside the block
    h=9
    print(h)
fn2()
print(h)

#Passing function as an argument to another function
def add1(a):
    return a+1
def sq(n):
    return n**2
num=int(input("enter a number: "))
print(sq(add1(num)))

#Lambda syntax
#lambda argument : expression

fun = lambda a,b : a+b
print(fun(5,6))


#filter(function,sequence)
# for each element of sequence function is called and give the true values

seq = [1,2,3,4,5]
filtered_output = filter(lambda x:True if x%2==0 else False,seq) #to get even numbers from list
print(filtered_output)
print(list(filtered_output))

#map(function,sequence)
# for each element of sequence function call and stores the result
mapped_output = map(lambda x:True if x%2==0 else False,seq) #to get even numbers from list
print(mapped_output)
print(list(mapped_output))

mapped_output = map(lambda x:x*2,seq) #to get even numbers from list
print(list(mapped_output))
