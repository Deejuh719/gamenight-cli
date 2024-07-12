### Vigenere Cipher (04.2024)

#### (named vignere_cypher.py)

1. A program to learn string manipulation from [FreeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/learn-list-comprehension-by-building-a-vigenere-cipher/step-1)
2. Takes a string and a key and returns a string of the encrypted text or vice versa
3. Cipher is currently buggy and will play with it to allow user input as well as encryption/decryption correctly in both directions (04.12.2024)

### Convert to Snake Case (04.2024)

1. A conversion program to learn about lists from [FreeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/learn-list-comprehension-by-building-a-case-converter-program/step-1)
2. Takes a string of PascalCase or camelCase and converts it to snake_case and adds it to the list
3. Modified main() and lines 28-32 to ask for user input, as well as introduce the program and print out examples of the program's output
4. Commented out lines 2-10 are the long version of what lines 14-18 do
5. Added a while loop to keep asking for user input, as well as a way to exit the program

### Bagels Game (06.26.2024)

1. This game is based on the code featured in the book "The Big Book of Small Python Projects".
2. It's base code is available [here](https://inventwithpython.com/bigbookpython/project1.html)
3. Alterations include:
   - Instead of printing out "Pico" "Fermi" and "Bagels" it will print P, F, B and is noted in the instructions
   - Included letters for a hexadecimal code option
   - Instead of 3-digit combinations, it's 4, and guess count is 20 (may up later)
   - Line 51 upper-cases the guess and the solution so that it can match and allow for a correct guess
   - Line 39 utilizes regex for comparing guesses
   - Lines 43-45 for quitting out without using CTRL+Z

### Birthday Paradox (06.27.2024)

1. This game is based on the code featured in the book "The Big Book of Small Python Projects".
2. It's base code is available [here](https://inventwithpython.com/bigbookpython/project2.html)
3. Alterations include:
   - Lines 99-112, allowing for multiple response options to print based on probability
   - Added match_count on lines 66, 70-71 for if a match in the birthday sim occurs
   - Edited print line on 78 to state that at least 1 person has a birthday on x-date
   - startOfYear begins in 1980 instead of 2001 because of bias
4. Was going to alter the amount of birthdays that can be matched or the amount of times the simulation is run, but that caused extreme latency on the runtime

### Vigenere Cipher (But Better) (06.27.2024)

#### (named vignerecipher.py)

1. Fully functional cipher that actually encrypts and decrypts based on user input
2. From "The Big Book of Small Python Projects", base code [here](https://inventwithpython.com/bigbookpython/project80.html)
3. Only thing I changed about this code was the title/intro to the cipher
4. Will use as an example to edit the first cipher from FreeCodeCamp

### Magic 8 Ball (07.12.2024)

1. Code built from scratch using guidance only from previous projects
2. Utilizes the random.randint() method to generate a random number between 1 and 20 correlating to the orignal 20 responses of a magic 8 ball
3. Requires user input for a question and prints out a random response, will continue to do so until user inputs "quit"
4. Will potentially add a way to save the responses to a text file in the future as well as change into an HTML format so that it can be viewed on a webpage
