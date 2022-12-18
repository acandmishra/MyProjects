#Q1
grades=[9,7,7,10,3,9,6,6,2]
a=len(grades)
print(grades.count(7)) # 1
grades[a-1]=4 #2
print(grades)
print(max(grades)) # 3
sorted(grades) # 4
print(grades)
print(sum(grades)/a) # 5
print("______________________________________________________________")
#Q2
L=[12,"hello",45,67,89,"hello","bye","enter","hello","python","end"]
x=len(L)
for i in range(x):   # 1
    if(L[i]=="hello"):
        print(i)
for i in L:   # 2
    if(i == "hello"):
        L.remove(i)
        print(L)
        
for i in range(3): # 3
    L.append("Hello")
    print(L)
#Q3
for i in range(1,101):
    if(i%2==0 or i%3==0 or i%5==0):
        pass
    else:
        print(i)
# Q4
set={10,20,30,40,50}
rem={10,20,30} # making a set with elements to be deleted 
set.difference_update(rem) #using difference_update method to remove the rem elements and update set with unique values
print(set)
# Q5
set1 = {10,20,30,40,50}
set2 = {60,70,80,90,50}
if(set1.isdisjoint(set2)):
    print("elements not same")
else:
    print("same elements found")
print(set1)