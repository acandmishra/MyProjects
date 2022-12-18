# a="Acand" # here "a" is a string which is iterable
# i=(a.__iter__()) # __iter__() is a method available for iterable object which gives us the iterator
# print(i.__next__()) # iterator can be moved forward using __next__() method 
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())

def gen(n):    # this is a generator as it gives the value on fly instead of saving it before hand
    for i in range(n): # range() is also a type of generator
        yield i

g=gen(3)
print(g)
print(g.__next__())
print(g.__next__())