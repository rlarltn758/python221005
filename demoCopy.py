# demoCopy.py
# shallow copy
a = [1,2,3]
b = a
a[0] = 38
print(a)
print(b)
print(id(a))
print(id(b))

# deep copy
print("-- deep copy")
a = [1,2,3]
b = a[:]
a[0] = 38
print(a)
print(b)
print(id(a))
print(id(b))

import copy
a = [100,200,300]
b = copy.deepcopy(a)
a[0] = 101
print(a)
print(b)
print(id(a))
print(id(b))

print(5/2)
print(5//2)
print(5%2)
print(4%2)