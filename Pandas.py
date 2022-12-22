import pandas as pd
import matplotlib.pyplot as plt
A=pd.Series(["a","b","c"])
print(A)
print(type(A))
print(A.describe()) # describe function gives the following in numbers and top is in
# count,unique,top,frequency
B=pd.DataFrame([["a","b","c"],["d","e","f"]])
print(B)
print(type(B))
print(B.describe()) #gives description coloumnwise


#Working with csv files
# data = pd.read_csv("https://www.bit.ly/imdbratings",nrows=10,usecols=["title"])
data = pd.read_csv("https://www.bit.ly/imdbratings")
print(data)
print(data.head()) #by default only starting 5 rows will be printed
print(data.tail()) #by default only ending 5 rows will be printed 
# in above passing arguments will print that many rows 
print(data.columns)
print(data.shape)
print(data.dtypes)
print(data[data.duration>200])
print(data[(data.duration>200) & (data.genre=="Drama")]) #bitwise and is used ie.&
print(data.duration) # dot operator is used to access the coloumn specified and if the coloumn name 
# is having space the write in quotes inside square brackets
print(data[(data.duration>200) & ((data.genre=="Drama")|(data.genre=="Action"))])
# the above can also be done as below
print(data[data.duration>200 & data.genre.isin(["Drama","Action","Romance"])])
print(data.genre.unique()) # returns a list with each element being unique , here we get all unique genre
print(data.genre.nunique()) # it gives the number of unique elements in the column used to make call
print(data.genre.value_counts()) # it gives the counts of each unique element for the column used to make the call
print(data.genre.value_counts(normalize=True)) # to get the same above thing as percentage
print(data.genre.value_counts().plot()) # use plot with the value_counts to get plotting of data
print(data.genre.value_counts().plot(kind="bar")) #kind is used to specify the type of graph  we want \\ this gives vertical bar
print(data.genre.value_counts().plot(kind="barh")) #same as above but gives horizontal bars instead of vertical
print(data.genre.value_counts().plot(kind="pie")) #write only pie inside plot to get a pie chart
print(data.describe()) # using describe() on csv gives followings
# count,mean,std,min,25%,50%,75%,max
print(data.groupby("genre").describe()) # it does the same thing as above but for each unique element fro the passed column
print(X:=data.groupby("genre").agg(["min","max","mean"])) # .agg is used to run multiple functions on data frame at same time
# above will perform min,max,mean on all the columns that are type int
print(X:=data.groupby("genre").duration.agg(["min","max","mean"])) # this will perform the passed operatins only on duration column
X.to_csv("PandasF2.csv")
print(data.actors_list.str.contains("Khan")) # this will give boolean for each entry in actors_list
print(data[data.actors_list.str.contains("Khan")]) # this will give all the entries in actors_list with khan in it

