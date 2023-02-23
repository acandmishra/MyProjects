space = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]
map = [0,0,0,0,0,0,0,0,0]
print(map)

print("welcome to the tic tac toe")
if(input("A enter your symbol (X/O):")=="X"):
    print("symbol for B is:O")
    S1="X"
    S2="O"
else:
    print("symbol for B is:X")
    S1="O"
    S2="X"
A=set({})
B=set({})
def show(map):
    print(map[0:3])
    print(map[3:6])
    print(map[6:9])
def check(player,super):
    for i in super:
        if(i.issubset(player)):
            if(player==A):
                show(map)
                print("A is winner")
            else:
                show(map)
                print("B is winner")
            exit(0)


Turn = 1
i=0
j=0
while 0 in map:
    if Turn == 1:
        i+=1
        print("chance of A")
        a=int(input("enter your index:"))
        map[a]=S1
        A.add(a)
        if i>=3:
            check(A,space)
        show(map)
        Turn=0
    else:
        j+=1
        print("chance of B")
        b=int(input("enter your index:"))
        map[b]=S2
        B.add(b)
        if j>=3:
            check(B,space)
        show(map)
        Turn=1