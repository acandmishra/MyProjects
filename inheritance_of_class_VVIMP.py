class Person():
    def __init__(self,first,age):
        self.name=first
        self.age=age
    def ShowName(self):
        print(self.name)
    def ShowAge(self):
        print(self.age)
class Student(Person):
    def __init__(self,studentname,studentage,studentid):
        self.id=studentid
        Person.__init__(Student,studentname,studentage)
    def identity(self):
        print(self.id)
A=Person("Ronnie","20")
A.ShowName()
A.ShowAge()
B=Student("Shilpa","21","202")
B.ShowName()
B.ShowAge()
B.identity()