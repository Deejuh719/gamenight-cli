"""Bagels Game
A deductive logic game where you must guess a number based on clues.
This game is based off the code featured in the book "The Big Book of Small Python Projects".
It's also available here https://nostarch.com/big-book-small-python-programming
"""

import random, re, time

NUM_DIGITS = 5 # Number of digits in the number to guess, can change later
MAX_GUESSES = 20 # Number of guesses allowed, can change later

def main(gamenight_main):
    print('''Bagels Game, a game of deductive logic.
          by Al Sweigart
          Toyed with by Khadijah Surratt github.com/deejuh719
          
          I am thinking of a sequence of a {} digit/letter combination with no repetition.
          The combination will be determined by which version you choose to play (letters, numbers, or both). 
          Try to guess what it is. Here are some clues:
          When I say:     That means:
          P = Pico            One digit is correct but in the wrong position.
          F = Fermi           One digit is correct and in the right position.
          B = Bagels          No digit is correct.

          For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.'''.format(NUM_DIGITS))
    print('\n')

    while True: # Main game loop
        print('Do you want to play with (L)etters only, (N)umbers only, or (B)oth? Press (Q) to quit.')
        print("Player's choice: ")
        player_choice = input('> ').lower()

        if player_choice == 'q':
            print('Quitting game... See ya around.')
            time.sleep(1)
            return gamenight_main()

        if player_choice == 'l':
            print('You have chosen to play with letters only.')
            secretNum = getSecretNum('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        elif player_choice == 'n':
            print('You have chosen to play with numbers only.')
            secretNum = getSecretNum('0123456789')
        elif player_choice == 'b':
            print('You have chosen to play with both letters (A-F) and numbers (0-5).')
            secretNum = getSecretNum('012345ABCDEF')
        else:
            print('Invalid choice. Please try again.')
            time.sleep(1)
            continue

        time.sleep(1)
        print('I have a code in mind.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))
        print('\n')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess or quit
            while True:
                print('Guess #{}:'.format(numGuesses))
                guess = input('> ')

                if guess.lower() == 'q':
                    print('Quitting game... See ya around.')
                    time.sleep(1)
                    return gamenight_main()

                if len(guess) != NUM_DIGITS:
                    print('Please enter exactly {} characters.'.format(NUM_DIGITS))
                elif player_choice == 'l' and not re.match(r'^[A-Z]{' + str(NUM_DIGITS) + '}', guess, re.IGNORECASE):
                    print(f'Please enter only letters A-F.') # If letters only, throws error to do only letters
                elif player_choice == 'n' and not re.match(r'^[0-9]{' + str(NUM_DIGITS) + '}', guess):
                    print(f'Please enter only digits 0-9.') # If numbers only, throws error to do only numbers
                elif player_choice == 'b' and not re.match(r'^[A-F0-5]{' + str(NUM_DIGITS) + '}', guess, re.IGNORECASE):
                    print(f'Please enter only digits 0-5 and letters A-F.') # If both, specifies the range of both letters and numbers to use
                else:
                    break

            clues = getClues(guess, secretNum)
            print(clues)

            if guess.upper() == secretNum.upper():
                print('You got it in {} guesses!'.format(numGuesses))
                break # They're correct, so break out of this loop
            
            numGuesses += 1

            if numGuesses > MAX_GUESSES:
                print('You are out of guesses.')
                print('The answer was {}.'.format(secretNum))

        # Ask player if they want to play again
        print('Wanna play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing. See ya around!')
    time.sleep(1)
    return gamenight_main()

def getSecretNum(characters):
    """Returns a string made up of NUM_DIGITS unique random characters."""
    numbers = list(characters)
    random.shuffle(numbers) # Shuffle them into random order

    #Get the first NUM_DIGITS characters in the list for the secret number:
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
        if guess[i].upper() == secretNum[i].upper():
            # A correct digit is in the correct place.
            clues.append('F')
        elif guess[i].upper() in secretNum.upper():
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