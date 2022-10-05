# function1.py
# define function

def setValue(newVal):
    # local value
    x = newVal
    print("inner function:", x)

# call
retValue = setValue(5)
print(retValue)

# define function
def swap(x,y):
    return y,x

# call
print(swap(3,4))

# LGB(local, global, builtin)
x = 10
def func(a):
    return x+a

# call
print(func(1))

def func2(a):
    x = 5
    return x+a

print(func2(1))

print("-- immutal format")
a = 1.2
print(id(a))
a = 2.3
print(id(a))

print("-- mutal")
lst = [1,2,3]
print(id(lst))

lst = [1,2,3]
print(id(lst))

lst.append(4)
print(id(lst))