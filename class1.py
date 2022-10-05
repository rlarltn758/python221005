#class1.py

# 1) define Class(type)

class Person:
    age = None
    name = ""
    # init method
    def __init__(self):
        self.name = "default name"
    
    # instance method
    def print(self):
        print("my name is {0}".format(self.name))


# create instance
p1 = Person()
p2 = Person()
p1.name = "jenwochi"
p1.gender = "A"

# call method
p1.print()
p2.print()
print(p1.gender)