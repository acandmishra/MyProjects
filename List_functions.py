L=[1,7,12,4,5]
L.sort() # sorts the list in ascending order , passing --> reverse=True will sort in reverse order
print(L)
L.append("hello") #string will be added at end
L.append(3) #number will be added at the end
print(L)
L.extend("Hello") # takes stirng only and then breaks it into characters and add at the end
print(L)
L.reverse() # reverses the whole list
print(L)
L.remove("hello") # takes string and numbers both and removes them from the list
print(L)
L.insert(1,3) # takes index,element
print(L)
L.pop() # writing simply pop removes the last element and passing index will remove element from that index
print(L)
print(L.count(7)) # counts the occurence of element passed
L.clear() # clears all the elements in the list and upon printing gives --> []
print(L)
# del(L[2]) #deletes the list index passed
# print(L)
# del(L) # deletes the complete list and printing list after this will give error
# print(L)
