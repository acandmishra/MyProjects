import numpy as np

arr = np.array([1,2,3,4,5]) 
print(arr)
print(arr.shape) #shape is a lable which gives the number of rows and coloumn in the array
arr = np.array([1,2,3,4,5],np.int8) 
# this will set dtype = int 8 , helps in memory management , or we could have given int =32 or 64
print(arr)

arr = np.array([[1,2,3,4,5],[34,56,3,1,0]],np.int64) # by using double square brackets we make a 2d array
print(arr[0,2])
print(arr)
print(arr.shape)
print(arr.dtype) # gives the type of array used ie. 8 or 32 or 64 bits
arr[0,2]=100 #it will change the element value at index 0,1 
print(arr)
print(arr.size) #to print the size of array
#there are five mechanism to create NumPy array
# first one ie to make array with tuple and list is used above

arr = np.array({2,4,3,6,7})
print(arr.dtype) #for arrays made using sets , the dtype is "object"

arr = np.array(range(1,8)) #using range function inside array function to create 1D array
print(arr)

# NumPy functions to create arrays:-
zeros = np.zeros((2,2))
print(zeros)

arr = np.arange(1,8) # used to create an array using the range passed but without the array function
print(arr)

arr = np.linspace(1,3,10) # takes starting index , ending index inclusive and gives 10 elements equally space from 1 to 3
print(arr)
arr = np.linspace(1,10,10)
print(arr)

empty = np.empty((2,3)) #it creates array with random values , the order is passed as argument inside brackets

identity = np.identity(20)
print(identity) 
print("\n")
print("below is a 4,4 matrix:")
arr = np.ones((4,4))
print(arr)
print("below is the above matrix reshaped to 8,2:")
print(arr.reshape((8,2)))
print("using ravel:")
print(arr.ravel()) #used to convert any array into 1D
print("using flatten")
print(arr.flatten()) # used for the same purpose as ravel
#using above wont change the actual array instead returns a new 1D array.
print("below is a 2D matrix")
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print("below is the sum of above matrix with axis=0,ie.coloumn wise")
print(arr.sum(axis = 0))
print("below is the sum of above matrix with axis=1,ie.row wise")
print(arr.sum(axis = 1))
print(arr.T) # prints the transpose of matrix T
for item in arr.flat: # using flat will return us an iterable unit which has elements row wise
    print(item)
    print("dimention of the array is:")
print(arr.ndim) # this tells the dimention of the array
print("\n")
print("the size is :",arr.size) # it tells the total number of elements in the array

print(arr.nbytes) # tells how much bytes is consumed by array
print("\n")


# some methods in NumPy
arr = np.array([[1,2,3],[4,3,67],[9,87,56]])
print("max(index):",arr.argmax()) # gives the index of maximum element
print("min(index):",arr.argmin()) # gives the index of minimun element
print(arr.argsort()) # gives the list of indexes in the order in which the resulting array will be sorted , bh default sorting is row wise
print("\n")
print("min element:",arr.min())
print("max element:",arr.max())
print("sorted array flattened:",arr.sort())

# Arithmetic operations in NumPy
print("sum in NumPy")
A = np.array([1,2,3])
B = np.array([4,5,6])
print(A+B)
print(A-B)
print(A*B)
print(np.sqrt(A))
print(np.sqrt(B))

arr = np.array([[1,2,3],[7,8,9],[6,4,2]])
print(np.where(arr<5)) #it returns first list of rows and second of coloumn
print(type(np.where(arr<5)))
print("no. non zeros are:",np.count_nonzero(arr)) #it gives the number of non zero elements
print(np.nonzero(arr))

# visit scipy.org for NumPy array methods and attribute
print("#_____________________#")



# More Operations on NumPy Matrix/Array
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
c = np.array([[11],[12],[13],[14],[15]])
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
print(np.unique(z,return_counts=True)) # returns an obj with original array and then again another array with each element as count of the original unique elements of original array
print(np.unique(z,return_index=True)) # returns the index of first occurence of the elements


#NumPy Slicing and Indexing
# a[row start:stop:interval,coloumn start:stop:interval]
import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0,0]) # +ve indexing starts from 0 on both axis
print(arr[-2,-2])
# same indexing rules as for lists
print(arr[:2]) # prints form 0 to 1 excludes 2
print(arr[:,:]) # prints complete matrix
print(arr[:,:2]) # prints all rows but only coloumns from 0 to 1 , 2 is excluded
print(arr[::2,::2]) # all rows and coloumns but with step of 2
print(arr[[1,2],[1]]) # takes only specified rows and specified coloumns || same coloumn is used for both rows when only one coloumn is specified
print(arr[[1,2],[1,2]]) # as there are two rows and two coloumns specified adj pairing hapens , ie.(1,1) and (2,2)
# similarly negative indexing can also be specified
print(arr[::-1,::-1]) #reversed the matrix both along row and coloumn


print(np.ptp(arr)) #it gives max-min
print(np.where(arr%2==0,"even","odd")) # where(condition,"when true","when false")