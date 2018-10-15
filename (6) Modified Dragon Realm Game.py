import random
import time

def displayIntro():
    print('''You are in a land full of dragons.  In front of you,
you see four caves.  In one cave, the dragon is friendly and will share his treasure with you.
In another cave, a different dragon is greedy and hungry, and will eat you on sight.  In a third cave, you will fall into a bottomless pit.
In the fourth and final cave, you will find a letter containing valuable life advice.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3' and cave!= '4':
        print('Which cave will you go into? (1, 2, 3, or 4)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('You step into the entrance and...')
    print()
    time.sleep(2)

    friendlyCave = ('')
    unfriendlyCave = ('')
    pitCave = ('')
    letterCave = ('')
    
    unfriendlyCave = random.randint(1,2)
    if unfriendlyCave == 1:
        friendlyCave == 2

    if unfriendlyCave == 2:
        friendlyCave == 1

    pitCave = random.randint(3, 4)
    if pitCave == 3:
        letterCave == 4

    if pitCave == 4:
        letterCave == 3
    
    if chosenCave == str(friendlyCave):
        print('''A dragon appears and gives you his treasure!''')

    if chosenCave == str(unfriendlyCave):
        print('''A dragon appears and swallows you whole!''')

    if chosenCave == str(pitCave):
        print('''You fall into a bottomless pit and meet your demise.''')

    if chosenCave == str(letterCave):
        print('''You find a single letter in the middle of the vast cavern with a single sentence on it.
Valuable life advice: Avoid walking into random caves for maximum longevity.''')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
              displayIntro()
              caveNumber = chooseCave()
              checkCave(caveNumber)

              print('Do you want to play again? (yes or no)')
              playAgain = input()
