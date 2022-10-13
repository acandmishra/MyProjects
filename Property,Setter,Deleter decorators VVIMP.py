class Employee:
    def __init__(self,FN,LN):
        self.FN=FN
        self.LN=LN
        # self.email=f'{FN}_{LN}@gmail.com'
    @property  # we used decorator which helps to print the email without calling the function 
    def PrintEmail(self):
        if self.FN==None or self.LN==None:
            return "email not available,move to setter"
        return f'{self.FN}_{self.LN}@gmail.com'  #this is how we can change the name by making a separate function
    @PrintEmail.setter
    def PrintEmail(self,str):
        name = str.split("@")[0]
        self.FN=name.split("_")[0]
        self.LN=name.split("_")[1]
    @PrintEmail.deleter
    def PrintEmail(self):
        self.FN=None
        self.LN=None
        return print("deleted")

A=Employee("Mark","Fintch")
# print(A.email)
# A.FN="john"     doing this will not change the name because the name is set under the init which happens as soon as the object is created
# print(A.email)
# print(A.PrintEmail())
# A.FN="John"   
# print(A.PrintEmail())    we are running a function here PrintEmail()


print(A.PrintEmail)
A.FN="John"   
print(A.PrintEmail) # just name of the function insted of calling it is required as we have used decorator "@property"
# its like we have converted the PrintEmail() function into a property so no need for calling....

# now if we want to give value directly to the function we use setter...
A.PrintEmail="Piggy_Potty@gmail.com" # from here the string will be passed to the setter and the names wil be assigned
print(A.PrintEmail)

# del A.PrintEmail this will not delete coz it can not find a function in the class to delete it...
del A.PrintEmail
print(A.PrintEmail)