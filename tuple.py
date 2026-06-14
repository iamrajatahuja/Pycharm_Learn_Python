t1=("Hello",2,3.5,True,None,[1,2,3],(1,2))
print(t1)
print(t1[1])
#tuple is immutable and tuple slicing will be same as lists/strings
#we can't add,remove or modify tuple values, but we can read

t2=10,20,30,40,5
print(t2, type(t2))

print(t1+t2)
print(t2*2)
print(30 in t2)
print(t2.index(30))
print(t2.count(30))
print(min(t2))
print(sum(t2))

l1=[1,2,3]
t3=tuple(l1)
print(t3)

l1=list(t3)
print(l1)