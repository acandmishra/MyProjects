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
print(np.where(arr%2==0,"even","odd"))