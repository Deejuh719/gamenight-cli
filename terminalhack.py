import sys
import random
import time

# Character fillers
FillerChars = '~!@#$%^&*()_+-={}[]|;:,.<>?/'

with open('terminal-words.txt') as wordList:
    WORDS = wordList.readlines()
for i in range(len(WORDS)):
    WORDS[i] = WORDS[i].strip().upper()


def main(gamenight_main):
    # Run hacker game
    directions = (
        "Let's hack into the terminal!\n"
        "You have four attempts to guess the correct password and hack into the system.\n"
        "When you guess incorrectly, you will get a hint as to how many letters are in \n"
        "the correct location.\n"
        "Example: If the password is \"MONITOR\" and you guess \"CONTAIN\", you will get a \n"
        "hint that says \"2 out of 7\" because 'ON' is in the right location.\n"
        "Good luck! May the tech gods be with you."
    )
    print('* ~ ' * 21)
        # "Types out" the directions
    for char in directions:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()
    print('* ~ ' * 21)

    while True:
        input('Press Enter to begin...')

        gameWords = getWords()
        computerMemory = getComputerMemoryString(gameWords)
        secretPassword = random.choice(gameWords)
        winner = 'A C C E S S  G R A N T E D'

        print(computerMemory)
        # Starting with 4 tries and counting down
        for triesLeft in range(4, 0, -1):
            playerMove = askForPlayerGuess(gameWords, triesLeft)
            if playerMove == secretPassword:
                # "Types out" winning message
                for char in winner:
                    print(char, end='', flush=True)
                    time.sleep(0.05)
                print('\nPlay again? (Y or N)')
                if not input('> ').upper().startswith('Y'):
                    gamenight_main()
                    return
                else:
                    break
            else:
                numMatches = numMatchingLetters(secretPassword, playerMove)
                print(f'{numMatches} out of {len(secretPassword)}')  # Set to len for when I update password list
        else:
            print(f'Out of tries. The password was "{secretPassword}".')
            print('Play again? (Y or N)')
            if not input('> ').upper().startswith('Y'):
                gamenight_main()
                return

def getWords():
    # Returns a list of 12 words from the list that could be the password
    secretPassword = random.choice(WORDS)
    words = [secretPassword]

    # Find two words that have no matching letters
    # < 3 is used since the password is already in words
    while len(words) < 3:
        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 0:
            words.append(randomWord)
    # Find 2 words that have 3 matching letters, but give up at 500
    # tries if enough can't be found
    for i in range(500):
        if len(words) == 5:
            break  # Found 5 words, so break out of loop
        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 3:
            words.append(randomWord)

    # Find at least 7 words that have at least one matching letter
    # Give up at 500 tries if enough can't be found
    for i in range(500):
        if len(words) == 12:
            break  # Found 12 words, so break out of loop
        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) != 0:
            words.append(randomWord)

    # Add any random words until there are 12 words
    while len(words) < 12:
        randomWord = getOneWordExcept(words)
        words.append(randomWord)

    # Shuffle the list of words
    random.shuffle(words)

    assert len(words) == 12
    return words

def getOneWordExcept(blocklist=None):
    # Returns random word from words that isn't in blocklist
    if blocklist is None:
        blocklist = []
    
    while True:
        randomWord = random.choice(WORDS)
        if randomWord not in blocklist:
            return randomWord
        
def numMatchingLetters(word1, word2):
    # Returns number of matching letters in two words
    return sum(1 for a, b in zip(word1, word2) if a == b)

def getComputerMemoryString(words):
    # Returns string representing 'computer memory'
    # Pick one line per word to contain a word, 16 lines split into 2 halves
    linesWithWords = random.sample(range(16*2), len(words))
    # Starting memory address (cosmetic)
    memoryAddress = 16 * random.randint(0, 4000)

    # Create 'computer memory' string
    computerMemory = []  # Will contain 16 strings, one for each line
    nextWord = 0  # Index in words of the word to put into a line
    for lineNum in range(16):  # The lines in 'computer memory'
        # Create half a line of filler chars
        leftHalf = ''.join(random.choice(FillerChars) for _ in range(16))
        rightHalf = ''.join(random.choice(FillerChars) for _ in range(16))

        # Fill in password from words:
        if lineNum in linesWithWords:
            # Find random place in line to place the word
            insertionIndex = random.randint(0, 9)
            # Insert word
            leftHalf = (leftHalf[:insertionIndex] + words[nextWord] +
                        leftHalf[insertionIndex + 7:])
            nextWord += 1  # Update word put in half of line
        if lineNum + 16 in linesWithWords:
            # Find random place in line to place the word
            insertionIndex = random.randint(0, 9)
            # Insert word
            rightHalf = (rightHalf[:insertionIndex] + words[nextWord] +
                         rightHalf[insertionIndex + 7:])
            nextWord += 1  # Update word put in half of line

        computerMemory.append(f'0x{memoryAddress:04x}  {leftHalf}    0x{memoryAddress + (16*16):04x}  {rightHalf}')
        memoryAddress += 16  # Jump from (ex:) 0xe680 to 0xe690
    # Each string in computerMemory is joined into one large string
    return '\n'.join(computerMemory)

def askForPlayerGuess(words, tries):
    # Let player enter password guess
    while True:
        print(f'Enter password guess ({tries} Tries Remaining)')
        guess = input('> ').upper()
        if guess in words:
            return guess
        print(f'That is not one of the words listed above. \n Try entering "{words[0]}" or "{words[1]}"')

if __name__ == '__main__':
    try:
        import gamenight
        main(gamenight.main)
    except KeyboardInterrupt:
        gamenight_main()  # When Ctrl-C is pressed, end the program.