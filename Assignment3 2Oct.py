# Q1
a=input("enter a string:")
l = len(a)
b= (a[0:2] + a[l-2:])
print(b)

# Q2
x=a[0]
print(x+(a[1:].replace(x,"$")))

# Q3
str=input("enter a string:")
len=len(str)
if len<3:
    print(str)
    pass
else:
    if str.endswith("ing")==True:
        print(str+"ly")
    else:
        print(str+"ing")

# Q8
lis = ["howdyh","deed","byebye","let's go","hmmh"]
count=0
for i in lis:
    if(len(i)>=4 and i[0]==i[-1]):
        count +=1
print(count)




