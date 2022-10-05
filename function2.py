# function2.py
# return intesection char
from cgi import test
from itertools import combinations
from time import time


def intersect(pre, post):
    result = []
    for x in pre:
        if x in post and x not in result:
            result.append(x)
    return result

# call
print(intersect("HAM", "SPAM"))

def change(x):
    x[0] = "H"

wordlist = ["J","A","M"]
change(wordlist)
print("after calling function:", wordlist)

# 
wordlist = ["J","A","M"]
def change(x):
    x1 = x[:]
    x1[0] = "H"

change(wordlist)
print("after calling function:", wordlist)

# 
g = 1
def testScopr(a):
    #global g
    g = 2
    return a+g

#
print(testScopr(1))
print("global g:", g)

def times(a=10,b=20):
    return a+b

print(times())
print(times(5))
print(times(5,6))

def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

print(connectURI("credu.com", "80"))
print(connectURI(port="80", server="credu.com"))