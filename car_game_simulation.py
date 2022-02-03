print("car game simulation")
a=""
b=False
c=False
while True:
    a=input(">>>").upper()
    if a=="HELP":
        print('''
to start car-->start
to stop car-->stop
to quit playing-->quit ''')
    elif a=="START":
        if(b==True):
            print("car already started")
            continue
        print(">>>car started")
        b=True
    elif a=="STOP":
        if(c==True):
            print("car already stopped")
            continue
        print(">>>car stopped")
        c=True
    elif a=="QUIT":
        break   
    else:
        print("i don't know this")
print("game ended")
exit    
