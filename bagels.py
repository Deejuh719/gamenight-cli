"""Bagels Game
A deductive logic game where you must guess a number based on clues.
This game is based off the code featured in the book "The Big Book of Small Python Projects".
It's also available here https://nostarch.com/big-book-small-python-programming
"""

import random
import re

NUM_DIGITS = 4 # Number of digits in the number to guess, can change later
MAX_GUESSES = 15 # Number of guesses allowed, can change later

def main():
    print('''Bagels Game, a game of deductive logic.
          by Al Sweigart
          Toyed with by Khadijah Surratt github.com/deejuh719
          
          I am thinking of a sequence of a {} digit/letter combination with no repetition.
          The combination will be made up of digits in the range 0 to 9 and letters A to F. 
          Try to guess what it is. Here are some clues:
          When I say:     That means:
          P = Pico            One digit is correct but in the wrong position.
          F = Fermi           One digit is correct and in the right position.
          B = Bagels          No digit is correct.

          For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.'''.format(NUM_DIGITS))
    print('\n')

    while True: # Main game loop
        secretNum = getSecretNum()
        print('I have a number in mind.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))
        print('\n')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess
            if not re.match(r'^[A-Fa-f0-9]$'.format(NUM_DIGITS), guess):
                print('Guess #{}:'.format(numGuesses))
                guess = input('> ')

            if guess.lower() == 'quit':
                print('Quitting game... See ya around.')
                return

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess.upper() == secretNum.upper():
                break # They're correct, so break out of this loop
            if numGuesses > MAX_GUESSES:
                print('You are out of guesses.')
                print('The answer was {}.'.format(secretNum))

            # Ask player if they want to play again
        print('Wanna play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing. See ya around!')

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789ABCDEF') # Create a list of digits 0 to 9 and letters A to F
    random.shuffle(numbers) # Shuffle them into random order

    #Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess.upper() == secretNum.upper():
        return 'Congrats! You guessed it!'
    
    clues = []

    for i in range(len(guess)):
        guess_upper = guess[i].upper()
        secret_upper = secretNum[i].upper()
        if guess_upper == secret_upper:
            # A correct digit is in the correct place.
            clues.append('F')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues.append('P')
    if len(clues) == 0:
        return 'B' # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)
    
# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()