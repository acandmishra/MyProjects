s={1,2,3,4,5,6,7}
s1=s.copy() # to copy set
print(s1)

t={1,2,3,8,9,10}
print(s.difference(t)) # gives unique elements in s
print(s)
print(t.difference(s)) # gives unique elements in t
print(t)
# s.difference_update(t) #updates the difference of s-t in s
# print(s)
# s.discard(7) # the passed element is removed from the set if the element passed is not present it will move to next line
# print(s)
# s.remove(1) # gives error if the passed element is not present
# print(s)
# s.pop() # simply pops the 1st element , mind it the first element and not the last one
# print(s)
print(s.intersection(t)) # gives the intersection of s and t
print(s.isdisjoint(t)) # gives true or false regarding disjoint
a={1,2,3}
b={1,2,3,4,5,6,7}
print(b.issuperset(a)) # gives true or false regarding superset
print(a.issuperset(b))
print(a.issubset(b)) #gives true or false regarding subset
print(b.issubset(a))
print(s.symmetric_difference(t)) # gives all the unique elements of both sets
# shorthand for above is s^t
print(s^t)
s.symmetric_difference_update(t) # updates the values of symmetric difference in set s
print(s.union(t)) #prints the union of both sets
#shorthand for above is s|t
print(s|t)
a.update("hello") # updates the set character wsie in anyorder ie some charcters at start some in mid some at last
print(a)