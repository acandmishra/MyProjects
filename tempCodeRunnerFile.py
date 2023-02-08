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