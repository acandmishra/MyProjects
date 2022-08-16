list1=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
list2=[]
for num in list1:
    if num not in list2:
        list2.append(num)
print(list2)