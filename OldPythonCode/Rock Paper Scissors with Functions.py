__author__ = 'Rinisha'
__date__ = '11/8/2015'
choices =  {"rock": 1, "paper" :2,"scissors":3 }
import random

USER_WON = "Congratulations!! you won! The computer Selected: :"
USER_LOST="Sorry you Lost. The computer Selected:  "
TIE = "The game is tied. The computer Selected:  "
score = 0
lives = 1


def computer_choice():
    n = random.randint(1,3)
    return n


def player_choice():
    choice = input('Enter your choice: Rock or Paper or Scissor(as a string:')
    return choices.get(choice.lower(),0)

def verify(userInput, computerInput):
    if (userInput==computerInput):
        '''score = score + 0
        lives = lives - 0'''
        printM(TIE, computerInput)
    else:

        if (userInput == 1):
            if (computerInput == 2):
                '''score = score + 0
                lives = lives - 1'''
                printM(USER_LOST, computerInput)

            else:
               ''' score = score +1
                lives = lives +0'''
               printM(USER_WON, computerInput)
        elif (userInput == 2):
            if (computerInput == 3):

                '''score = score + 0
                lives = lives - 1'''
                printM(USER_LOST, computerInput)
            else:
                '''
                score = score + 1
                lives = lives - 0
                '''
                printM(USER_WON, computerInput)
        else:
            if (computerInput == 1):
                '''
                score = score + 0
                lives = lives - 1
                '''
                printM(USER_LOST, computerInput)
            else:
                '''
                score = score + 0
                lives = lives +0'''
                printM(USER_WON, computerInput)
        if (lives == 0):
            print "You Ran Out Of Lives! Score is:"
'''for i in range(1,100,1):
    print choices
    '''

def printM(message, choice,):
    '''
    fp.open(message, "a")
    fp.append (message)'''
    fp = open("results.txt" ,"a")
    for name, value in choices.items():
        if value == choice:
            print message+" "+name.upper()
            fp.write(message+" "+name.upper())
    fp.close()
userInput=0

while userInput==0:
    userInput= player_choice()

verify( userInput, computer_choice())
