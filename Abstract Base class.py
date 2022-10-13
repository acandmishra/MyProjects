from abc import ABC,abstractmethod # abstractmethod and ABC helps us to make it compulsory for all the daughter class to have a particular method or else the programme will show error
class Resl(ABC): # objects for this can't be made
    @abstractmethod
    def Sub(self):
        print()
        return 0
class Dost(Resl):
    def Sub(self):
        return 10
    def Hello(self):
        return(5+7)
        
A=Dost()
print(A.Hello())       