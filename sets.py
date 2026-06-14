#sets are non-sequential collection of items means no indexing/slicing
#No duplicate items

s1={"i",2,3.5}
print(s1)
print(type(s1))
print(len(s1))
s2={1,2,1,2,3}
print(s2)
print(2 in s2)

# sets are unordered
t1 = (4,3,2,1,4)
t1 = set(t1)
print(t1)
t1 = list(t1)
print(t1)
t1 = set(t1)
print(t1,type(t1))

# sets are mutable
s2.add(-1)
print(s2)
s2.remove(2)
print(s2)
#remove gives error if we try to remove element which is not present in set, but discard doesn't
s2.discard(4)
print(s2)

stu1={1,2,3,4,5}
stu2={3,4,7,8}
stu3={9,10}

# intersection-common
inter=stu1.intersection(stu2)
print(inter)
inter=stu1 & stu2
print(inter)
inter=stu1.intersection(stu2,stu3)
print(inter) #gives empty set - set() as output

#union - all
un = stu1.union(stu2,stu3)
print(un)
un = stu1 | stu2 | stu3
print(un)

# difference in sets
dif = stu1.difference(stu2)
print(dif)
dif = stu1 - stu2
print(dif)

#symmetric difference - apart from intersection elements
sdif = stu1.symmetric_difference(stu2)
print(sdif)
sdif = stu1 ^ stu3
print(sdif)

# Frozen sets are immutable - no add or remove
fs1 = frozenset({1,2,3,4,5})
fs2 = frozenset({3,4,7,8})
print(fs1, type(fs1))

print(fs1 & fs2)
print(fs1 | fs2)
print(fs1 - fs2)
print(fs1 ^ fs2)