# higher order functions are those which takes a function as argument and an iterable also and returns an iterable too 

def cube(x):
    return (pow(x,3))
# print(cube(10)
# MAP
# above is the code for cube which can be used for different value of x but if we want to use the function over iterable then what??
# here comes map function in use

lis=[2,3,4,5,6]
print(list(map(cube,lis))) #this returns an object of map

#FILTER
# it can take a function and apply it to all elements in a iterable
#  the function it takes is the one according to which the elements of iterable will be checked and unsatisfactory elements will be removed
def check(a):
    return (a>3)
print(list(filter(check,lis)))

# REDUCE
# it reduces the given iterable by applying the fuction passed to the first two elements only 
# and then continuing the same for thus formed new iterable
from functools import reduce
def sum1(a,b):
    return (a+b)
print(reduce(sum1,lis))

