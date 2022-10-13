a=[1,1,1,2,2,3,4,5,6,7,7,8,9]
l = len(a)
s = set(a)
for i in s:
    print(f"frequency of {i} is:{a.count(i)}")

