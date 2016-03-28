from random import randint
print( 'GHOST DOOR GAME' )
score=0
feeling_brave= True

while feeling_brave:
    ghost_door = randint(1, 3)   
    print(' There are three doors ahead...')
    print(' There is a ghost behind one...')
    print(' Do not run into the ghost!' )
    print(' Which door will you open?')
    door= input(' 1, 2 ,or 3: ')
    door_num = int(door)
    if door_num == ghost_door:
        print(' Ghost! ')
        feeling_brave= False

    else:
        print(' No ghost!' )
        print(' You enter the next room')
        score = score + 1
        print(' Your score is ', score)
print(' RUN AWAY ')
print(' YOU SCORED:', score)
