def function1(xyz):  # this function will return Press,but the contents of Press is not printed coz its just returned
    def Press():
        print("hello")
        xyz()
        print("bye")
    return Press

def Welcome():
    print("welcome home")
Welcome=function1(Welcome) #here Welcome will go in function1 and then go inside Press and then fuction1 
# will return Press and that returned Press will be stored in Welcome and after this if Welcome is called then apparently Press is being called 
Welcome()

#OR
# @ function1
# def Welcome():
#     print("welcome home")
# above line 15 and code in line 10 does same thing
