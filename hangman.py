from random import choice
import time

def select_word(): # selects a word from a list of words.txt
    with open("words.txt", mode="r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()

def get_player_input(guessed_letters): # gets player input and validates it
    while True:
        player_input = input("Guess a letter: ").lower() # sets player input to lowercase
        if _validate_input(player_input, guessed_letters):
            return player_input

import string

def _validate_input(player_input, guessed_letters): # validates player input
    return (
        len(player_input) == 1 # checks that player input is only one character
        and player_input in string.ascii_lowercase # checks that player input is a lowercase letter
        and player_input not in guessed_letters # checks that player input has not already been guessed
    )

def join_guessed_letters(guessed_letters): # joins guessed letters into a string
    return " ".join(sorted(guessed_letters)) # sorts the letters alphabetically

def build_guessed_word(target_word, guessed_letters): # builds the guessed word
    current_letters = [] 
    for letter in target_word: # loops through the target word
        if letter in guessed_letters: # checks if the letter is in the guessed letters
            current_letters.append(letter) # if it is, it adds it to the current letters
        else:
            current_letters.append("_") # if it is not, it adds an underscore
    return " ".join(current_letters) # joins the current letters into a string

def draw_hanged_man(wrong_guesses): # draws the hanged man
    hanged_man = [
        r"""
    -----
    |   |
        |
        |
        |
        |
        |
        |
        |
        |
    -------
""",
        r"""
    -----
    |   |
    O   |
        |
        |
        |
        |
        |
        |
        |
    -------
""",
        r"""
    -----
    |   |
    O   |
   ---  |
    |   |
    |   |
        |
        |
        |
        |
    -------
""",
        r"""
    -----
    |   |
    O   |
   ---  |
  / |   |
    |   |
        |
        |
        |
        |
    -------
""",
        r"""
    -----
    |   |
    O   |
   ---  |
  / | \ |
    |   |
        |
        |
        |
        |
    -------
""",
        r"""
    -----
    |   |
    O   |
   ---  |
  / | \ |
    |   |
   ---  |
  /     |
  |     |
        |
    -------
""",
        r"""
    -----
    |   |
    O   |
   ---  |
  / | \ |
    |   |
   ---  |
  /   \ |
  |   | |
        |
    -------
""",
    ]
    print(hanged_man[wrong_guesses]) # prints the hanged man

MAX_INCORRECT_GUESSES = 6

def game_over(guesses_taken, target_word, letters_guessed): # checks if the game is over
    return (
        guesses_taken == MAX_INCORRECT_GUESSES # checks if the player has run out of guesses
        or set(target_word) <= letters_guessed # checks if the player has guessed all the letters
    )

def play_hangman():
    target_word = select_word() # selects a word
    guessed_letters = set() # sets the guessed letters to an empty set
    guessed_word = build_guessed_word(target_word, guessed_letters) # builds the guessed word
    guesses_taken = 0 # sets the guesses taken to 0
    print("""Let's play Hangman!\n
            I'll think of a word,
            and you guess what it is. \n""") # prints the title
    time.sleep(1) # waits for 1 second

    # Game loop

    while not game_over(guesses_taken, target_word, guessed_letters): # loops until the game is over
        draw_hanged_man(guesses_taken) # draws the hanged man
        print(f"""Incorrect guesses: {guesses_taken} out of {MAX_INCORRECT_GUESSES}\n
                The word is: {guessed_word} \n
                Current guessed letters: \n
                {join_guessed_letters(guessed_letters)}\n""")

        player_guess = get_player_input(guessed_letters) # gets the player's guess
        if player_guess in target_word: # checks if the player's guess is in the target word
            print("It's in the word!\n")
        else:
            print("Sorry. Not this one.\n")
            guesses_taken += 1 # adds one to the guesses taken
        guessed_letters.add(player_guess) # adds the player's guess to the guessed letters
        guessed_word = build_guessed_word(target_word, guessed_letters) # builds the guessed word

# Game over

    draw_hanged_man(guesses_taken) # draws the hanged man
    if guesses_taken == MAX_INCORRECT_GUESSES: # checks if the player has run out of guesses
        print(f"Sorry, you lost. The word was {target_word} \n")
        print("Play again? y or n") # asks if the player wants to play again
        if input("") == "y": # if yes, it plays again
            play_hangman()
            time.sleep(1)
        else:
            print("Thanks for playing") # if no, prints thanks and exits
            time.sleep(1)
            exit()
    else:
        print(f"Congratulations, you won. The word was: {target_word} \n")
        time.sleep(1)
        print("Play again? y or n")
        if input("") == "y":
            play_hangman()
            time.sleep(1)
        else:
            print("Thanks for playing")
            time.sleep(1)
            exit()

if __name__ == "__main__":
    play_hangman()