Dict={
    "Key1":"Value1",
    "Key2":"Value2",
}

# Q1
Dict["Key3"]="Value3"
print(Dict)

# Q2
D1={"A":"1","B":"2"}
D2={"a":"3","b":"4"}
print(D1|D2)

# Q3
a=input("enter the value for searching:")
# get method returns value if key is found else returns default message
print(Dict.get(a,"element not found"))  # get is a return type function therefore it has to be printed 

# Q4
D3={1:"X",2:"Y",3:"Z"}
print(sum(D3))  # keys should be integers

# Q5
D1.pop("A")
print(D1) 

# Q6
D4={5:"h",6:"e",2:"ll",0:"o"}
print(sorted(D4.items())) # using items()
print(D4.items())

# Q7
D5={1:"a",2:"b",3:"c",4:"d",5:"a",6:"d"}




# Q8
D6={"aa":"a","bb":"b","cc":"c","dd":"d"}
print(D6.keys())
print(list(D6.keys()))
print(list(D6.values()))
print(len(D6))

# Q9
D7={}
for i in range(1,16):
    D7[i]=i*i
print(D7)    