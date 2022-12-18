def Occupation(*args,**kwargs):  # Kwargs takes in a dictionary and args is sort of list
    for x in args:
        print(x)
    for key,value in kwargs.items(): # items is used to access each entry in a dictionary
        print(f"the value of {key} is:{value}")

Channels=["mkbhd","mwtb","tg","st","jip","jre"]
salary={"teachers":"10 lacs",
        "students":"20thousand"}

Occupation(*Channels,**salary)#giving asterix is important ,doing so passes the tuple/list in place of args 
