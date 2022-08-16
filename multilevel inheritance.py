class Dad:
    score=100
    marks=50
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
print(Ram.score)