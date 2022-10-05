class Person:
    num_person = 0
    # init method
    def __init__(self):
        self.name = "default name"
        #Person.num_person += 1
    
    # instance method
    def print(self):
        print("my name is {0}".format(self.name))


p1 = Person()
p2 = Person()
p2.num_person = 10
p3 = Person()
print("instance count : {0}".format(Person.num_person))
print(p1.num_person)
print(p2.num_person)

Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)