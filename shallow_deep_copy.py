# This concept is applied on mutable datatypes
import copy

#shallow copy
l1 = [1,2.5,[10,20,30],"Hi"]
l2 = copy.copy(l1)

l1[0]=5
l1[2][0]=60

print(f"{l1}", id(l1))
print(f"{l2}", id(l2))  #main index value of l2 not changed but internal nested list values changed

# To overcome this problem, we have deep copy in which inner list also get different address

l2 = copy.deepcopy(l1)
l1[0]=500
l1[2][0]=600
print(f"{l1}", id(l1))
print(f"{l2}", id(l2))

#This same concept works for dictionaries as well