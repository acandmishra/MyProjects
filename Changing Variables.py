class Dad:
    variable = 10
    @classmethod
    def change(cls,new_variable):
        cls.variable = new_variable
D = Dad()
D.variable = 30
print(D.variable)  # we changed the variable with the help of instance/object D.
print(Dad.variable)
# from above we see that chnaging the class variable through the instance does not changes class variable 
# instead it creates a variable of same name for the instance through which it was called.
D.change(100)
print(D.variable)
print(Dad.variable)
# using the decorator @classmethod will enable us to change the class variables with the help of instances too.
