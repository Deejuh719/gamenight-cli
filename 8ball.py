import random
import time

def main():
    print("\u2058Hello, I am the ~~Magic \u2787 Ball~~!\u2058")
    time.sleep(1)
    print("Ask me anything and I'll show you your future!")
    print("Type 'quit' to exit the game.")
    print("\n")
    time.sleep(2)
    while True: # Main game loop
        print("Focus and ask your question to the Magic 8 Ball.")
        time.sleep(1)
        print("Just don't shake me though, I am still your computer...")
        
        # Question is user input
        question = input('> ')
        # Generate a number between 1 and 20
        answer = random.randint(1, 20)

        # If user types quit, exit the game
        if question.lower() == "quit":
            print('Thank you for consulting the Magic 8 Ball, goodbye!')
            print("\n")
            time.sleep(0.5)
            print("Magic 8 Ball: Created by K Surratt found on https://github.com/deejuh719")
            print("\n")
            break  # Break out of the while loop

        # Use if statements to print answer based on number generated
        elif answer == 1:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("It is certain ")
            print('\n')
        elif answer == 2:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("It is decidedly so")
            print('\n')
        elif answer == 3:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("Without a doubt")
            print('\n')
        elif answer == 4:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("Yes, definitely")
            print('\n')
        elif answer == 5:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("You may rely on it")
            print('\n')
        elif answer == 6:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("As I see it, yes")
            print('\n')
        elif answer == 7:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("Most likely")
            print('\n')
        elif answer == 8:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("Outlook good")
            print('\n')
        elif answer == 9:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("Yes")
            print('\n')
        elif answer == 10:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("Signs point to yes")
            print('\n')
        elif answer == 11:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("Reply hazy try again")
            print('\n')
        elif answer == 12:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("Ask again later")
            print('\n')
        elif answer == 13:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("Better not tell you now")
            print('\n')
        elif answer == 14:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("Cannot predict now")
            print('\n')
        elif answer == 15:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("Concentrate and ask again")
            print('\n')
        elif answer == 16:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("Don't count on it")
            print('\n')
        elif answer == 17:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("My reply is no")
            print('\n')
        elif answer == 18:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("My sources say no")
            print('\n')
        elif answer == 19:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("Outlook not so good")
            print('\n')
        elif answer == 20:
            print("\u00abShaking...\u00bb")
            time.sleep(1)
            print("Very doubtful")
            print('\n')

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()