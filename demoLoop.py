# demoLoop.py

val = 5
while val > 0:
    print(val)
    val -= 1

# using for in sequence type
lst = [1,2,3,4,5,6,7,8,9,10]
for item in lst:
    print(item)

d = {"apple": 100, "orange":200, "kiwi":300}
for k,v in d.items():
    print(k,v) 

for i in [2,3,4,5,6]:
    print("{0}단".format(i))
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(i,j,i*j))


for i in [1,2,3,4,5,6,7,8,9,10]:
    print("*" * i)

print("break")
lst = [1,2,3,4,5,6,7,9,10]
for i in lst:
    if i % 2 == 0:
        break
    print("item:{0}".format(i))

print("continue")
lst = [1,2,3,4,5,6,7,9,10]
for i in lst:
    if i % 2 == 0:
        continue
    print("item:{0}".format(i))

rangeIdex = range(10)
print(rangeIdex.step)

# list 
lst = list(range(1,11))
print([i**2 for i in lst if i>5])
tp = ("apple", "oragne", "kiwi")
print( [len(i) for i in tp])
d = {100:"apple", 200:"kiwi"}
print( [v.upper() for v in d.values()])

print("--no flitering")
lst=[10,25,30]
for item in filter(None, lst):
    print(item)


print("-- flitering")
def getBiggerThan20(i):
    return i > 20

lst=[10,25,30]
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)
