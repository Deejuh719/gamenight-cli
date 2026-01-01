import random, sys, time

def main(gamenight_main):
    print('Welcome to Quick Draw!')
    time.sleep(1)
    print("""Let's test your reflexes! When you see the word 'DRAW' you have 0.5 seconds to 
          press Enter to draw your imaginary gun and shoot. 
          If you're too slow or too fast, you lose. 
          Good luck!""")
    time.sleep(0.5)
    print('Press Enter to begin...')

    while True:
        input("It's High Noon...")
        time.sleep(random.randint(20, 50) / 10)
        print('DRAW')
        drawTime = time.time()
        input() # Shouldn't call until Enter is pressed
        drawDuration = round(time.time() - drawTime, 3)

        if drawDuration < 0.01 :
            # If player draws too quickly, they lose
            print('You drew and shot before the "DRAW" appeared!')
            time.sleep(0.5)
            print('You lose.')
            time.sleep(0.5)
        elif drawDuration > 0.5:
            # If player draws too slowly, they lose
            print('You drew and shot too slowly.')
            print('{:.3f} seconds to be exact...'.format(drawDuration))
            time.sleep(0.5)
            print('You lose. Practice more.')
            time.sleep(0.5)
        elif drawDuration <= 0.25:
            print('You drew and shot in {:.3f} seconds.'.format(drawDuration))
            time.sleep(0.5)
            print("You're crazy fast!")
            time.sleep(0.5)
        elif drawDuration <= 0.3:
            print('You drew and shot in {:.3f} seconds.'.format(drawDuration))
            time.sleep(0.5)
            print("Lookin' good! You're a natural.")
            time.sleep(0.5)
        elif drawDuration <= 0.499:
            drawDuration = round(drawDuration, 3)
            print('You drew and shot in {:.3f} seconds.'.format(drawDuration))
            time.sleep(0.5)
            print("You almost didn't make it! Try better next time!")
            time.sleep(0.5)
        print('Wanna play again? (Y/N)')
        answer = input('> ').upper()
        if answer.startswith('N'):
            print('Thanks for playing!')
            time.sleep(0.5)
            gamenight_main()


if __name__ == '__main__':
    main()