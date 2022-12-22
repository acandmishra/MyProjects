class Student:
    variable = 10
    def __init__(self,name,age,std):
        self.name = name
        self.age = age
        self.std = std
    @classmethod
    def change(cls,new_variable):
        cls.variable = new_variable
    @classmethod
    def struct(cls,str):
        # split = str.split("-")
        # return cls(split[0],split[1],split[2])
        # or
        return cls(*str.split("-")) # used the *args 

A = Student("Rahul","21","4th") # this will crate new objects and their instance variables
B = Student("Rohan","19","2nd")

C = Student.struct("Raj-20-3rd")

print(A.name)
print(B.name)
print(C.name)
