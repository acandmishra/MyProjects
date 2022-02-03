num=[1,33,54,66,78,80,88,108,120]
print(b:=len(num))
large = num[0]
for i in range(b):
    if (num[i]>large):
        large = num[i]
    else:
        large=large
print(f"the largest number is {large}")