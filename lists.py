l1=[1,2,"Hello",4.5,None,True,3]
print(l1[-1])
print(l1[2:4:1])

# List is mutable so operations change the existing list
l2=[0,3]
print(id(l2))
l2[1]=9
print(id(l2))
l3=[2,3,4,[5,6]]
print(l1+l2+l3)
print(l2*4)
print(l2)

l4=l3.copy()  #it performs shallow copy
print(l3,id(l3))
print(l4,id(l4))
l3[3][0]=50
print(l3,id(l3))
print(l4,id(l4))

l8=[1,2,[3,4]]
l9=l8
print(l8,id(l8))
print(l9,id(l9))
l8[2][0]=50
print(l8,id(l8))
print(l9,id(l9))






print(l2.append("Hi"))
print(l2)
l2.insert(2,"Hello")
print(l2)

l2.extend(["K","J",1])
print(l2)
l2.append(["K","L"])
print(l2)
l2.append("J")
print(l2)

l2.remove("J")
print(l2)
l2.pop(3)
print(l2)
l2.pop()
print(l2)
l2.pop(-1)
print(l2)

l2.reverse()
print(l2)

l5=[2,1,2,3]
l5.sort()
print(l5)
l5.sort(reverse=True)
print(l5)

l4=["zello","World","zello"]
l4.sort()
print(l4)
print(l4.count("zello"))
print(l4.count("Zello"))
print(l4.index("zello"))
print("zello" in l4)

num=[2,12,1.4,-4]
print(min(num))
print(sum(num))

l5=[1,2,[1,2,4,[5,6]]]
print(len(l5))
print(l5[-1][-1][0])