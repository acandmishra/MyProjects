class Library:
    BD1=["book1","book2","book3","book4","book5"]
    BD={}
    def exist(self,list,name):
            if ((name in list)== True):
                print("book exists")
                return True
            else:
                print("does not exist")
                exit()

    def lend(self,list):
        a=input("your name:")
        b=input("name of the book:")
        if (self.exist(list,b)==True):
            self.BD[a]=b
        else:
            print("book not found")

Ml=Library()
Ml.exist(Ml.BD1,"book1")
Ml.lend(Ml.BD1)
print(Ml.BD)