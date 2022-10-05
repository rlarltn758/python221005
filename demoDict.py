# demoDict.py

names = ("kim", "kisu")
print("id:%s, name:%s" %names)
print("id:%s, name:%s" %("kim","kisu"))

def calc(a, b):
    return a*b
    
# call
args = (5,6)
print(calc(*args))

# init dic
device = {"iphone": 5, "ipad":10, "windowTablet":20}
print(device["iphone"])
device["mac"] = 30
print(device)

# delete
del device["iphone"]
# modify
device["ipad"] = 12
print(device)

for i in device.items():
    print(i)

print(" ----- -----")
for k,v in device.items():
    print(k,v)

tp = (1,2,3)
list = list(tp)
list.append(4)

print(list)
print(tuple(list))
print(tp)

phone = {"kim":"111", "lee":"222", "park":"333"}
print("kim" in phone)
print("moon" in phone)

# copy reference
p = phone
p["monn"] = "1234"
print(p)
print(phone)
print(id(phone))
print(id(p))

# logical
print( 1 <2)
print( 1 == 2)
print( 1 != 2)
print( True and True and True)
print( True and True and False)
print( True or False or False)


