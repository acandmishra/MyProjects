list=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
for i in list:
    if(list.count(i)==2):
        del(list[i])
print(list)