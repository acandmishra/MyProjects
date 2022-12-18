import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
c = np.array([[11],[12],[13],[14],[15]])
print(c)
print(np.concatenate((a,b),axis=0)) # row wise
print(np.stack((a,b))) # row over row stacking , gives multi dimentional array
arr = np.array([[1,2,3],[4,5,6]])
print(np.append(arr,7)) # flatten arr and appends the passed element to the end
print(np.vstack(a)) # it stacks the x axis as y axis
print(np.hstack(c)) # it stacks the y axis as h axisprint

x=np.array([1,2,3,4,5,6])
print(np.split(x,2)) # splits the array into the number passed as argument , does not work if each part is not equal
y = np.array([[1,2],[3,4],[5,6],[7,8]])
print(np.vsplit(y,2)) # splits multi dimentional array according to the number passed
print(np.hsplit(y,2))

print(np.append(x,[7,8,9,10,11,12])) # append fucntion takes name of array and elements to be appended as arguments
print(np.append(y,[[9,10],[11,12],[13,14],[15,16]])) #will append each row to already existing row
print(np.insert(x,0,[100])) # (array,location,value) inserts 100 at index 0
print(np.insert(y,2,[999],axis=1)) # insert 999 at index 2 in every row
print(np.delete(y,0)) # flattens given matrix and deletes element at index 0
print(np.delete(y,0,axis=0)) # deletes 0th index along all horizontal axis
print(np.delete(y,0,axis=1)) # deletes 0th index along all vertical axis

z=np.array(["a","b","c","c","d","a","b"])
print(z)
print(np.unique(z)) # prints all the unique elemnets of given matrix
print(np.unique(z,return_counts=True)) # returns an obj with original array and then again another array with 
# each element as count of the original unique elements of original array
print(np.unique(z,return_index=True)) # returns the index of first occurence of the elements
