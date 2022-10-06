# 부모 클래스 정의
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
    def coding(self):
        print("현재 코딩중")
    def eating(self):
        print("현재 식사중")

# 자식 클래스 정의
class Student(Person):
    #덮어쓰기(재정의, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        # 명시적으로 부모 초기화 메서드 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1}, {2}, {3})".format(
            self.name, self.phoneNumber, self.subject, self.studentID))

# 자식 클래스 정의
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "221122")
#print( p.__dict__)
#print( s.__dict__)
p.printInfo()
s.printInfo()
s.coding()
s.eating()
