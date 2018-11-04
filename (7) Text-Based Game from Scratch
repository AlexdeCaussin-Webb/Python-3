#This game is called Meteoric.

import time
import random
import winsound

#Title Screen

print('  ___')
print(' /*  \\')
print('|   * |')
print(' \\___/')  
print('Meteoric: A post-apocalyptic escape game')
print('**It is advised to play this game with a maximized window.**')
print('Press [Enter] to play.')
input()

#Act 1 - Prologue
    
def DisplayIntro():       
    print('Post-Apocalyptia definitely isn\'t all it was cracked up to be.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('..')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('....')
    time.sleep(2)
    print('''...Shit, this whole world isn\'t what it was cracked up to be.
    We were sold some vision of a bright future full of opportunity as children.
    As we grew up, though, the fantastical world around us dissolved into one of suspicion and dread.''')
    print()
    print('Press [Enter]')
    input()

    print('''I was only five when it happened, but I can still remember the sound
    the impact made as clear as day...''')
    time.sleep(1.5)
    print()

    winsound.PlaySound('Russia Meteor sound shockwave.wav', winsound.SND_FILENAME)

    print('''And then my entire world was gone.  Thanks to the Impact Winter, soon most everyone else's world
    was gone too.''')
    time.sleep(1)
    print()
    print('''My family and I didn't last for long thanks to a gang of raiders. When I was ten my parents were killed and my brother and I
    were separated and sold off as slaves to different raider gangs around Crater Alley.  It's been eight years since then, and I'm now eighteen.
    I'm still a slave, but not for long. I've been cobbling together a nice-sized knife for some time now, and I'm going to make my escape. It's
    finally time.''')
    print()
    print('Press[Enter]')
    input()
    print()

#Act 2 - Cell block escape

def EscapeCell():
    print('''With my improvised knife ready, I survey my cell and the room outside of it. I haven't had a cellmate for a while, which is a blessing. I have a pile
of blankets on the floor to sleep on, and my dinner plate and fork are still near them. It's the middle of the night, so there's just the one guard sitting on a chair
outside of my cell, facing away and looking to be dozed off. The door leading in and out of the cell areas is closed. What should I do?''')
    print()
    print('''Press [Enter].''')
    input()
    print()
    print('''[1.] Try to wake the guard up.''')
    print('''[2.] Pick the fork and dinner plate up.''')
    print('''[3.] Try to kill the guard with your knife.''')
    print('''[4.] Try to pickpocket the cell keys off of the guard with your knife.''')
    print()
    
    action = ''
    while action != '1' and action != '2' and action != '3' and action != '4':
        print('''What action will you take? (1, 2, 3, or 4 then [Enter]).''')
        action = input()

    if action == '1':
        print('''You walk to the edge of your cell and tap the guard on the shoulder. After he wakes comes to, he gives you a dirty look
and jerks his shoulder away. He notices your knife. After fumbling around with the keys, he opens your cell door and enters, whereupon he begins to beat you bloody.''')
        #Failed ending 1
        print('''GAME OVER.''')

    if action == '2':
        print('''You pick the fork and dinner plate up and decide you have two choices from here:''')
        print()
        print('1: Throw the fork and dinner plate against the cell wall.')
        print('2: Throw the fork and dinner plate at the guard.')
        print()

        #Branching path 1
        
        action2 = ''
        while action2 != '1' and action2 != '2':
            print('''What action will you take? (1 or 2, then [Enter].''')
            action2 = input()

        if action2 == '1':
            print('''The guard jumps awake, startled. After focusing his eyes on you, he notices the fork and broken plate on the floor as well as your knife.
After fumbling around with the keys he opens your cell door and enters, whereupon he begins to beat you bloody.''')
            #Failed ending 2
            print('''GAME OVER.''')

        else:
            print('''The dinner plate and fork go right between the cell bars, nailing the guard in the back of the head! Unfortunately, this does nothing
besides waking him up and making him angry. After narrowing his eyes on you he fumbles around with his keys and opens your cell door, whereupon he
begins to beat you bloody.''')
            #Failed ending 3
            print('''GAME OVER.''')

    if action == '3':
        print('''You carefully tiptoe toward the guard. He is seated facing forward, away from you, and is still dozed off. You
gingerly slip your hand and knife through the bars and across his throat, but a sudden movement from the guard makes you gasp, waking him.
Jerking away, he fumbles around with his keys and opens your cell door, whereupon he begins to beat you bloody''')
        #Failed ending 4
        print('''GAME OVER.''')

    if action == '4':
        print('''You carefully tiptoe toward the guard. He is seated facing forward, away from you, and is still dozed off. You gingerly slip your hand
and knife through the bars and keyring hanging at the guard's hip.  You lift the knife, bringing the keyring off of its holster and...''')
        time.sleep(2)

        success = random.randint(1,5)
        if success == 1 or success == 3:
            print('''succeed in taking the keys! After carefully opening the cell door, you sneak out of the cell areas and escape the compound!
You are now free to carve out your own destiny in post-apocalyptica.''')
            #Victorious ending
            print('CONGRATULATIONS: YOU WIN!')
        else:
            print('''the keyring slips off of your knife! The guard wakes up at the sound of keys hitting the floor.
He focuses on you, realizes the situation, and fumbles with his keys to open your cell door. After doing so, he begins to beat you bloody.''')
            #Failed ending 5
            print('''GAME OVER.''')
        

PlayGame = 'yes'            
while PlayGame == 'yes' or PlayGame == 'y':
    DisplayIntro()
    EscapeCell()   

    print('PLAY AGAIN? (YES/NO)')
    PlayGame = input()





