T = int(input("enter passes:"))
for t in range(T):
    N=int(input())
    lis=[]
    arr=[int(i) for i  in (input(f"enter {N} digits:"))]
    for e in arr:
        c=0
        for x in arr:
            for y in arr:
                if(x==y):
                    continue
                if(abs(x-y)%e!=0):
                    c+=1
                else:
                    break
        if(c==(N*N)-N):
            lis.append(e)       
    print(min(lis))
