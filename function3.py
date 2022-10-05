# function3.py
# 가변인자

def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))

def userURLBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

print(userURLBuilder("credu.com", "80", id="kim", passwd="1234"))
print(userURLBuilder("credu.com", "80", id="kim", passwd="1234", \
    name="miki"))


g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print( (lambda x:x*x)(3))
print(globals())

lst=[10,25,30]
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)