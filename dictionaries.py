#dictionaries are mutable

d1 = {'milk':60, 'apple':70, 'banana':80, 'orange':90}
print(d1, type(d1), len(d1))
d1['milk']=65
print(d1['milk'])
d1['eggs'] =50 #adds item
print(d1)

print(d1.get('grape')) #gives value of key if present in dictionary else none as value if key is not present or default value
print(d1)

#membership operator - in - checks for key
print('eggs' in d1)

d2={'fruit':40, 'apple':200}
d1.update(d2)
print(d1)

d1.pop('milk')
print(d1)

groceries = {'milk':60, 'apple':70, 'banana':80,'milk':30}
print(groceries) #keys cannot be duplicated

#Allowed keys: str, int, float, bool, tuple
#not allowed keys: list, set, dict
# because keys can only be immutable data types

#values can be any datatype
d3={'fruit':40, 'apple':200, 'milk':{'cow':100,'buffalo':50}}
print(d3['milk']['cow'])

print(d3.keys())
print(d3.values(), type(d3.values()))
print(d3.items(), type(d3.items()))