def largest(num):
    print(b:=len(num))
    large = num[0]
    for i in range(b):
        if (num[i]>large):
            large = num[i]
        else:
            large=large
    print(f"the largest number is {large}")