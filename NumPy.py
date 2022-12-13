import numpy as np
c = np.array(1)
print(c.dtype)

a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a.ndim)
print(a.shape)

b=np.array(range(1,17))
print(b)

d=np.arange(1,21,0.5)
print(d)

e=np.linspace(1,10) #gives 50 equally spaced elements as items in array , on passing third arg that many equally spaced elements are created
print(e)

print(f:= 10**np.linspace(1,10,4))
print(g:= np.empty(5)) #for 1 d array
print(g:=np.empty((5,2))) #for 2d array

print(h:=np.ones(5)) #for 1d
print(h:=np.ones((5,3))) #for 2d
print(h:=np.zeros(5)) #for 1d
print(h:=np.zeros((5,2))) #for 2d


