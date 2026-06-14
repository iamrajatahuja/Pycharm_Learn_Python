#type conversion
x=5
y=input("Enter a number ")
print(str(x)+y)
print(x+int(y))
print(10+x)
print(type(y))

#Python 35 keywords
import keyword
print(keyword.kwlist)

#string
s="Hello World"
print("First and Last character and second last",s[0],s[-1],s[-2])
print("Python"*3)
print("Hello" in s)
print("  Hello World   ".strip() == s)
print(s.replace("l","L"))
print(s.replace("l","L",1))
# New string is created with string functions as string is immutable
print(s)
print(s.count("l"))
print(s.count("or"))
print(s.find("l")) #returns -1 if not found
print(s)
print(s.index("l")) #returns ValueError if not found
print(s.upper())
print(s.capitalize())
print(s.startswith("he"))
print(s[1:15:2])

#f-string
a=10
b=90
print(f"{s} and total is {a+b}.")