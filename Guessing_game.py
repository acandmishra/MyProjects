print('''       lets play some game
(you will get three chance to guess the number)''')
target = 7
guess_count=0
guess_limit=3
while (guess_count<guess_limit):
    guess=int(input("YOUR GUESS:"))
    if(guess==target):
        print("you won!")
        exit()
    guess_count += 1
print("you lost!!🙃")
