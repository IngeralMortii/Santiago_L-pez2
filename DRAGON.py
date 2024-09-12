#dragon.py

import random
import time

def displayIntro():
    print('''Hello? Wake up buddy!...we are in another world, and how it looks, in one full of dragons 
. . . !!! There is a dragon front of you!,
look! two caves. In the first cave, is possible that we may find something to calm him is friendly. 
At the other cave there will be nothing, and it is going to devour us!.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def victory():
    print('On our way, we found. . .a dragon?, it could be a baby dragon, possibly...there is an older dragon!, wait he is calming down, they leave...we managed to survive for now...')

def history():
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('Wait!!! there is the dragon...')
    print()
    time.sleep(2)

def checkCave(chosenCave):
    history()

    friendlyCave = random.randint(1, 2)
    
    if chosenCave == str(friendlyCave):
        victory()
    else:
        print('Gobbles you down in one bite!')
            
        print("There's a different ending to this story...")
        time.sleep(2)
        print("Would you like to see it? (yes or no)")
        ending = input()
        if ending == "yes":
            history()
            victory()
    
playAgain = 'yes'
while True:
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)
        print('Do you want to play again? (yes or no)')
        playAgain = input()
    if playAgain == "no":
        break