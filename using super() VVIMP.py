class A():
    classvar1="hello you pigs!"
    def __init__(self):
        self.classvar1="Acand"
class B(A):
    classvar1="hello you donkeys!"
    def __init__(self):
        super().__init__()
        self.classvar1="hello!!"

a=A()
b=B()
print(b.classvar1)
# the programme first searches for instance variables and then searches for the class variable 
# (https://www.youtube.com/watch?v=HfmFcj0NmHI)