import random
class Dice:
    def roll(self):
        list=[1,2,3,4,5,6]
        print(f"({random.choice(list)},{random.choice(list)})")
a=int(input("No. of throws:"))
for i in range (0,a):
    ROLL=Dice()
    ROLL.roll()