import eightball, blackjack, hangman, bagels, vigenerecipher
import time
import sys

displayMenu = [
                        (1, "Magic 8 Ball"),
                        (2, "Blackjack"),
                        (3,"Hangman"),
                        (4, "Bagels"),
                        (5, "Vigenere Cipher"),
                        (6, "Quit")
]

def main():
    while True:
        print("Welcome to the Game Night!")
        print("Here's your choices of games:")
        for number, game in displayMenu:
            print(f"{number}. {game}")
        game_choice = input('Enter the number of the game you want to play: ')
        if game_choice == '1':
            print('You have selected Magic 8 Ball.')
            time.sleep(1)
            eightball.main(main)
        elif game_choice == '2':
            print('You have selected Blackjack.')
            time.sleep(1)
            blackjack.main(main)
        elif game_choice == '3':
            print('You have selected Hangman.')
            time.sleep(1)
            hangman.main(main)
        elif game_choice == '4':
            print('You have selected Bagels.')
            time.sleep(1)
            bagels.main(main)
        elif game_choice == '5':
            print('You have selected Vigenere Cipher.')
            time.sleep(1)
            vigenerecipher.main(main)
        elif game_choice == '6':
            print('Maybe next time!')
            print('Lookout for more games and projects!')
            time.sleep(0.5)
            sys.exit()
        else:
            print('Invalid choice. Please try again.')
if __name__ == '__main__':
    main()