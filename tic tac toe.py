space = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]
map = [0,1,2,3,4,5,6,7,8]
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
def check(player,super):
    for i in super:
        if(i.issubset(player)):
            print(f"Winner is->{player}")


for i in range(1,8):
    print("chance of A")
    a=int(input("enter your index:"))
    map[a]=S1
    A.add(a)
    if i>=3:
        check(A,space)
    print(map)
    print("chance of B")
    b=int(input("enter your index:"))
    map[b]=S2
    B.add(b)
    if i>=3:
        check(B,space)
    print(map)