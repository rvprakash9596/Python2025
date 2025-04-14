# PROJECT 1: SNAKE, WATER, GUN GAME :: We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a python program capable of playing this game with the

'''
1 for snake
-1 for water
0 for gun
'''

import random
computer = random.choice([-1,0-1])
youstr=input("Enter Your Choice : ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}

you = youDict[youstr]

print(f"You Chose {reverseDict[you]} \nComputer Chose {reverseDict[computer]}")
if(computer==you):
    print("Its a Draw!")
else:
    if((computer-you)== -1 or  (computer-you)== 2):
        print("You Lose!")
    else:
        print("You Win!")