import sys, random, time

# Character fillers
FillerChars = '~!@#$%^&*()_+-={}[]|;:,.<>?/'

with open('terminal-words.txt', 'r') as f:
    words = f.readlines()
for i in range (len(words)):
    words[i] = words[i].strip().upper()

def main(): # Run hacker game
    directions = "Let's hack into the terminal!\nYou have four attempts to guess the correct password and hack into the system.\nWhen you guess incorrectly, you will get a hint as to how many letters are in \nthe correct location.\nExample: If the password is \"MONITOR\" and you guess \"CONTAIN\", you will get a \nhint that says \"2 out of 7\" because 'ON' are in the right location.\nGood luck! May the tech gods be with you."
    print('* ~ ' * 21)
    # "Types out" the directions
    for char in directions:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    print('* ~ ' * 21)
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
                print()
        else:
            numMatches = numMatchingLetters(secretPassword, playerMove)
            print('{} out of {}'.format(numMatches, len(secretPassword))) # Set to len for when I update password list
        print('Out of tries. The password was "{}".'.format(secretPassword))

def getWords():
    # Returns a list of 12 words from the list that could be the password
    secretPassword = random.choice(words)
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
            break # Found 5 words, so break out of loop
        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 3:
            words.append(randomWord)

    # Find at least 7 words that have at least one matching letter
    # Give up at 500 tries if enough can't be found
    for i in range(500):
        if len(words) == 12:
            break # Found 12 words, so break out of loop
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
    if blocklist == None:
        blocklist = []
    
    while True:
        randomWord = random.choice(words)
        if randomWord not in blocklist:
            return randomWord




if __name__ == '__main__':
    main()