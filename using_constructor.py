class Person:
    def __init__(self,name):#this is a constructor(init means initialisation) , self refers to the object
        self.name=name
    def talk(self):
        print(f"hey {self.name} lets talk")

b=input("what's your name:")
Person1=Person(b)
print(Person1.name)
Person1.talk()