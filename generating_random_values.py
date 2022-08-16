import random
for i in range(3):
   print(random.random()) # generates random value between 0 and 1 ie. [0,1).
   print(random.randint(10,20)) # generates random value between the range passed , here between 10 and 20


members=["a","b","c","d","e"]
print(leader:=random.choice(members)) # choice() picks random value from the items in list  