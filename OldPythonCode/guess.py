import random
guesses =0


print("Hi my name is Rinisha what's yours???")
myName= input();
print('well hi '+  myName+ ' I am thiunking of a number 1-20')
number = random.randint (1,20)

while guesses < 6 :
    print("take a guess")
    guess= input()
    guess = int(guess)
    guesses = guesses +1

    if guess < number:
        print (' sorry too low')
    if guess > number:
        print('too high sorry')
    if guess == number:
        print (' good job ' + myName + " you guessed it in " + guesses + 'guesses')

    
       
