#Guess the number game where the program tells you if the number is higher or lower

import random
mysteryNumber = random.randrange(1,21,1)
while True:
    numberGuess = int(input('I am thinking of a number, can you guess it? It is between 1 and 20 '))
    while numberGuess > mysteryNumber:
        numberGuess = int(input('that number is too high, guess again! '))
    while numberGuess < mysteryNumber:
        numberGuess = int(input('that number is too low, guess again! '))
    print('You guessed the number {} is what I was thinking of! Let\'s play again, I am thinking of a new number.'.format(mysteryNumber))
    mysteryNumber = random.randrange(1,21,1)