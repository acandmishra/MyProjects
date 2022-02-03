class Point:    # we defined a class 
    def move(self):  # functions defined inside the class are  called methods 
        print("move")
    def draw(self):
        print("draw")


point1=Point() # this is the syntax to define the objects
point1.draw() # dot operator is used to use methods with the object
point1.x=10 # we gave attribute to the object////attributes are like variables defined for that object
print(point1.x)