# public
# private
# protected

class Dad():
    score=100
    marks=50
    _protected=999 #single underscore tells that the variable is protected
    __private=777 #double underscore tells that the variable is private
    def Daddy(self):
        print(f"Dad bod {self.score}")
class Son(Dad):
    score=25
    def Sonny(self):
        print(f"son bod{self.score}")
class GrandSon(Son):
    score=10
    def Gsonny(self):
        pass

Ram=Dad()
shyam=Son()
taam=GrandSon()
print(shyam._protected) # protected variables can't be used outside the python file in which they are defined , all the daughter classes within the same file can use it
print(Ram._Dad__private) # private variables can't be used by any class except the parent class and they also have different naming while accessing them
# Object._ClassName__VariableName