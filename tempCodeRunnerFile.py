import pandas as pd
import matplotlib.pyplot as plt
A=pd.Series(["a","b","c"])
print(A)
print(type(A))
print(A.describe()) # describe function gives the following
# count,unique,top,frequency
B=pd.DataFrame([["a","b","c"],["d","e","f"]])
print(B)
print(type(B))
print(B.describe()) #gives description coloumnwise