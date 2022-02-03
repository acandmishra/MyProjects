class animals:
    def hello(self):
        print("hello ! We are animals")

# after the class name we write inherited class in brackets
# inheritance:-to use methods from parent class 
class dog(animals):  
    def bark(self):  
        print("bark")
   
class cat(animals):
    def meow(self):
        print("meow")

dog1=dog()
dog1.hello() # method of animals class
dog1.bark() # method of dog class
# inheritance makes it possible to use the same piece of code again and again