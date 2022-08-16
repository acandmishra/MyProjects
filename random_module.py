import random
print(a:=random.randrange(100))
print(a:=random.randrange(100))
print(a:=random.randrange(100)) 
print(a:=random.randrange(100))
print(a:=random.randrange(100)) 
print(a:=random.randrange(100))
print(a:=random.randrange(100))  
list = [10,6,4,11,1] 
print(random.choices(list,weights=(1,0,0,0,0),k=5))
# random.choices takes 3 arguments//name of sequence(tuple,list,range(),string)//weights OR cum_weights  of each item in string//size of list returned