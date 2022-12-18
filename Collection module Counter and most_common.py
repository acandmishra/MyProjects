import collections as c
a=[1,2,3,4,5,6,7,8,9,0,2,3,4,5,3,2,1,3,4,5,5,8,9,8,7,7,7,8,9,8,6,5]
print(c.Counter(a)) # gives dictionary about occurence of each unique element in list
print(c.Counter(a).most_common(1)) # giving 1 will return list with top most common 2 will return top 2....

# below is another method to do the same as above but without the use of any module
L=[1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,6,7,8,9]
print(max(set(L),key=L.count))  # max can take another arg on basis of which max is to be found...
# here on the basis of count of elements of list L