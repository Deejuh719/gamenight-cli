from random import choice
import time

word_categories = [
    ("abruptly", "vocabulary", "hard"),
    ("absurd", "vocabulary", "medium"),
    ("abyss", "nature", "medium"),
    ("affix", "grammar", "hard"),
    ("agnostic", "religion", "medium"),
    ("apple", "food", "easy"),
    ("askew", "vocabulary", "medium"),
    ("avenue", "urban", "easy"),
    ("awkward", "social", "medium"),
    ("azure", "colors", "medium"),
    ("bagpipes", "music", "hard"),
    ("bandwagon", "idioms", "medium"),
    ("banjo", "music", "easy"),
    ("bayou", "nature", "medium"),
    ("bear", "animals", "easy"),
    ("beardless", "appearance", "medium"),
    ("beekeeper", "occupations", "medium"),
    ("bikini", "clothing", "easy"),
    ("blizzard", "weather", "medium"),
    ("boggle", "games", "easy"),
    ("bookworm", "hobbies", "medium"),
    ("boxcar", "transportation", "medium"),
    ("boxful", "measurements", "hard"),
    ("bread", "food", "easy"),
    ("buckaroo", "western", "hard"),
    ("buffalo", "animals", "easy"),
    ("buffoon", "personality", "medium"),
    ("build", "actions", "easy"),
    ("buzzard", "animals", "medium"),
    ("buzzing", "sounds", "easy"),
    ("buzzwords", "business", "medium"),
    ("caliph", "history", "hard"),
    ("camel", "animals", "easy"),
    ("candelabra", "object", "medium"),
    ("chair", "furniture", "easy"),
    ("chambermaid", "occupations", "medium"),
    ("chameleon", "animals", "medium"),
    ("cobweb", "nature", "easy"),
    ("cockiness", "personality", "medium"),
    ("coconut", "food", "easy"),
    ("create", "actions", "easy"),
    ("croquet", "sports", "medium"),
    ("crypt", "mystery", "easy"),
    ("curacao", "geography", "hard"),
    ("cycle", "science", "easy"),
    ("daiquiri", "food", "hard"),
    ("discover", "action", "medium"),
    ("dizzying", "sensations", "medium"),
    ("duplex", "housing", "medium"),
    ("dwarves", "fantasy", "medium"),
    ("embezzle", "crime", "hard"),
    ("equip", "general", "easy"),
    ("espionage", "mystery", "hard"),
    ("euphoria", "emotions", "medium"),
    ("evolution", "science", "medium"),
    ("exodus", "history", "medium"),
    ("faking", "behavior", "easy"),
    ("fishhook", "outdoors", "easy"),
    ("fixable", "general", "medium"),
    ("fjord", "geography", "hard"),
    ("flapjack", "food", "medium"),
    ("flopping", "movement", "easy"),
    ("fluffiness", "texture", "medium"),
    ("flyby", "aviation", "medium"),
    ("frog", "animals", "easy"),
    ("fountain", "architecture", "medium"),
    ("foxglove", "nature", "hard"),
    ("frazzled", "emotions", "medium"),
    ("frizzled", "cooking", "medium"),
    ("fruit", "food", "easy"),
    ("fuchsia", "colors", "hard"),
    ("funny", "emotions", "easy"),
    ("gabby", "personality", "medium"),
    ("galaxy", "space", "easy"),
    ("galvanize", "science", "hard"),
    ("gazebo", "architecture", "medium"),
    ("giaour", "culture", "hard"),
    ("gizmo", "technology", "easy"),
    ("glowworm", "nature", "medium"),
    ("glyph", "language", "hard"),
    ("gnarly", "slang", "medium"),
    ("gossip", "social", "easy"),
    ("grogginess", "health", "medium"),
    ("haiku", "literature", "medium"),
    ("haphazard", "organization", "hard"),
    ("happy", "emotions", "easy"),
    ("honest", "personality", "medium"),
    ("hyphen", "punctuation", "medium"),
    ("icebox", "household", "easy"),
    ("ideal", "personality", "medium"),
    ("injury", "health", "easy"),
    ("ivory", "materials", "medium"),
    ("ivy", "nature", "easy"),
    ("jackpot", "gambling", "easy"),
    ("jaundice", "medical", "medium"),
    ("jawbreaker", "candy", "medium"),
    ("jaywalk", "urban", "easy"),
    ("jazziest", "music", "medium"),
    ("jazzy", "style", "easy"),
    ("jelly", "food", "easy"),
    ("jigsaw", "puzzles", "easy"),
    ("jinx", "superstition", "easy"),
    ("jiujitsu", "sports", "hard"),
    ("jockey", "sports", "easy"),
    ("jogging", "fitness", "easy"),
    ("joking", "humor", "easy"),
    ("jovial", "personality", "medium"),
    ("joyful", "emotions", "easy"),
    ("juicy", "taste", "easy"),
    ("jukebox", "music", "easy"),
    ("jumbo", "size", "easy"),
    ("kayak", "sports", "easy"),
    ("kazoo", "music", "easy"),
    ("keyhole", "household", "easy"),
    ("khaki", "colors", "medium"),
    ("kilobyte", "technology", "medium"),
    ("kiosk", "business", "medium"),
    ("kitsch", "art", "hard"),
    ("kiwifruit", "food", "medium"),
    ("klutz", "personality", "medium"),
    ("knapsack", "outdoors", "medium"),
    ("larynx", "anatomy", "hard"),
    ("lengths", "measurements", "easy"),
    ("lucky", "fortune", "easy"),
    ("luxury", "lifestyle", "medium"),
    ("lymph", "anatomy", "medium"),
    ("marquis", "nobility", "hard"),
    ("materialistic", "personality", "hard"),
    ("matrix", "math", "medium"),
    ("mattress", "furniture", "medium"),
    ("megahertz", "technology", "hard"),
    ("microwave", "appliances", "medium"),
    ("milk", "food", "easy"),
    ("milkshake", "food", "medium"),
    ("mnemonic", "memory", "hard"),
    ("mountain", "geography", "medium"),
    ("mouse", "animals", "easy"),
    ("mystify", "mystery", "medium"),
    ("nightclub", "entertainment", "medium"),
    ("nowadays", "time", "easy"),
    ("numbskull", "insults", "medium"),
    ("nymph", "mythology", "medium"),
    ("onyx", "geology", "medium"),
    ("ovary", "biology", "medium"),
    ("oxidize", "chemistry", "hard"),
    ("oxygen", "science", "easy"),
    ("pajama", "clothing", "easy"),
    ("panther", "animals", "medium"),
    ("pants", "clothing", "easy"),
    ("pasta", "food", "easy"),
    ("peekaboo", "games", "easy"),
    ("phlegm", "medical", "hard"),
    ("phone", "technology", "easy"),
    ("pixel", "technology", "easy"),
    ("pizazz", "style", "medium"),
    ("pneumonia", "medical", "hard"),
    ("polka", "music", "easy"),
    ("pshaw", "expressions", "hard"),
    ("psyche", "psychology", "medium"),
    ("puppy", "animals", "easy"),
    ("puzzling", "mystery", "medium"),
    ("quack", "sounds", "easy"),
    ("quail", "animals", "medium"),
    ("quaint", "style", "medium"),
    ("quarry", "geography", "medium"),
    ("quartz", "geology", "medium"),
    ("quicksand", "geography", "medium"),
    ("queen", "nobility", "easy"),
    ("queue", "organization", "medium"),
    ("quiet", "personality", "medium"),
    ("quips", "humor", "medium"),
    ("quiz", "education", "easy"),
    ("quote", "literature", "medium"),
    ("razzmatazz", "style", "hard"),
    ("realism", "style", "medium"),
    ("rhubarb", "food", "medium"),
    ("rhythm", "music", "medium"),
    ("rickshaw", "transportation", "medium"),
    ("river", "geography", "easy"),
    ("rookie", "personality", "easy"),
    ("schnapps", "drinks", "medium"),
    ("school", "architecture", "easy"),
    ("scissors", "tools", "easy"),
    ("scratch", "actions", "easy"),
    ("scream", "sounds", "medium"),
    ("serious", "personality", "medium"),
    ("shiv", "weapons", "medium"),
    ("shy", "personality", "easy"),
    ("sleep", "action", "easy"),
    ("snazzy", "style", "medium"),
    ("sphinx", "mythology", "medium"),
    ("spritz", "actions", "medium"),
    ("squawk", "sounds", "medium"),
    ("staff", "business", "easy"),
    ("strength", "attributes", "medium"),
    ("strengths", "attributes", "hard"),
    ("stretch", "actions", "easy"),
    ("stronghold", "military", "medium"),
    ("stymied", "obstacles", "hard"),
    ("subway", "transportation", "easy"),
    ("sugar", "food", "easy"),
    ("sundae", "food", "medium"),
    ("swim", "sports", "easy"),
    ("swivel", "movement", "medium"),
    ("syndrome", "medical", "medium"),
    ("thriftless", "finance", "hard"),
    ("thumbscrew", "torture", "hard"),
    ("topaz", "gemstones", "medium"),
    ("transcript", "education", "medium"),
    ("transgress", "behavior", "hard"),
    ("transplant", "medical", "medium"),
    ("twelfth", "numbers", "medium"),
    ("twelfths", "fractions", "hard"),
    ("unknown", "mystery", "easy"),
    ("unworthy", "judgement", "medium"),
    ("unzip", "actions", "easy"),
    ("uptown", "urban", "easy"),
    ("vacation", "holiday", "easy"),
    ("valley", "geography", "easy"),
    ("vaporize", "science", "medium"),
    ("vixen", "animals", "medium"),
    ("vodka", "drinks", "easy"),
    ("voodoo", "supernatural", "medium"),
    ("vortex", "physics", "medium"),
    ("voyeurism", "behavior", "hard"),
    ("walk", "transportation", "easy"),
    ("walkway", "architecture", "easy"),
    ("waltz", "dance", "easy"),
    ("wave", "nature", "easy"),
    ("wavy", "description", "easy"),
    ("waxy", "texture", "easy"),
    ("wellspring", "nature", "medium"),
    ("wheezy", "health", "medium"),
    ("whiskey", "drinks", "easy"),
    ("whizzing", "sounds", "medium"),
    ("whomever", "grammar", "hard"),
    ("wimpy", "personality", "easy"),
    ("witchcraft", "supernatural", "medium"),
    ("wizard", "fantasy", "easy"),
    ("woozy", "health", "medium"),
    ("wristwatch", "accessories", "medium"),
    ("wyvern", "mythology", "hard"),
    ("xylophone", "music", "medium"),
    ("yachtsman", "occupations", "hard"),
    ("yak", "animals", "medium"),
    ("yap", "sounds", "easy"),
    ("yippee", "expressions", "easy"),
    ("yoked", "farming", "medium"),
    ("youthful", "age", "easy"),
    ("yummy", "food", "easy"),
    ("zap", "sounds", "easy"),
    ("zephyr", "weather", "hard"),
    ("zero", "numbers", "easy"),
    ("zigzag", "shapes", "easy"),
    ("zilch", "numbers", "medium"),
    ("zillion", "numbers", "hard"),
    ("zip", "compression", "easy"),
    ("zipper", "clothing", "easy"),
    ("zodiac", "astrology", "medium"),
    ("zombie", "supernatural", "easy"),
    ("zoology", "science", "medium"),
    ("zucchini", "food", "easy"),
]

#def select_word(): # selects a word from a list of words.txt
    #with open("words.txt", mode="r") as words:
        #word_list = words.readlines()
    #return choice(word_list).strip()

def select_word(difficulty = None): 
    if difficulty: # if difficulty is not None, then filter the words by difficulty
        filtered_words = [word for word in word_categories if word[2] == difficulty]
    if not filtered_words: # if filtered_words is empty, then return None
        return choice([word[0] for word in word_categories])
    chosen_word = choice(filtered_words)
    return chosen_word[0], chosen_word[1]

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

def main(gamenight_main):
    print("""Let's play Hangman! \n
            Choose your difficulty (easy, medium, or hard).""") # prints the title
    while True:
        difficulty = input("Choose your level: ").lower() # gets the difficulty
        if difficulty in ["easy", "medium", "hard"]: # checks if the difficulty is valid
            break # breaks the loop
        print("Invalid difficulty. Try again.") # prints an error message
        time.sleep(1) # waits for 1 second
    target_word, category = select_word(difficulty = difficulty) # selects a word
    guessed_letters = set() # sets the guessed letters to an empty set
    guessed_word = build_guessed_word(target_word, guessed_letters) # builds the guessed word
    guesses_taken = 0 # sets the guesses taken to 0
    print(f"""You chose {difficulty}, let's go!\n
            I'll think of a word,
            and you guess what it is. \n""") # prints the title
    time.sleep(1) # waits for 1 second

    # Game loop

    while not game_over(guesses_taken, target_word, guessed_letters): # loops until the game is over
        draw_hanged_man(guesses_taken) # draws the hanged man
        print(f"""Incorrect guesses: {guesses_taken} out of {MAX_INCORRECT_GUESSES}\n
                Category is: {category}\n
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
            main(gamenight_main)
        else:
            print("Thanks for playing") # if no, prints thanks and exits
            time.sleep(1)
            return
    else:
        print(f"Congratulations, you won. The word was: {target_word} \n")
        time.sleep(1)
        print("Play again? y or n")
        if input("") == "y":
            main(gamenight_main)
        else:
            print("Thanks for playing")
            time.sleep(1)
            gamenight_main()

if __name__ == "__main__":
    main()