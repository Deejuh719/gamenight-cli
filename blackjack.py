import random, sys, time

# TO DO
# Dejank 10, Q cards, lines print wonky, when first card causes others to jank
# Edit hand on splitting: only accounts for hand2 not hand1 when betting
#   if hand2 is a push, full bet is returned, hand1 neglected entirely
#   if hand1 is lesser than dealer, hand2 neglected entirely
#   if bust on a hand, still asks to H,S,Q doesn't move to second hand automatically
#   only displays one hand not both
#   hand1/hand2 in a split will automatically draw a card even if you stood causing a bust - 9.18.24
#   maybe include a function that compares hand1 and 2 against dealer - 9.18.24
# Why does house win bet but player loses double when dealer has blackjack?
# Why does game continue when player has blackjack? doesn't continue on dealer blackjack - 9.18.24
# Player gets blackjack, but prints you win 1.5x bet and another statement of 1.0x bet, only returns 1.5x - 9.18.24


#Set up constants
HEARTS = chr(9829) #for '♥'
DIAMONDS = chr(9830) #for '♦'
SPADES = chr(9824) #for '♠'
CLUBS = chr(9827) #for '♣'
BACKSIDE = 'backside'

def main(gamenight_main):
    print("""Let's Play Blackjack!
          
          Goal: 
            Get as close to 21 as possibly without going over.
          House Rules:
            [K]ings [Q]ueens and [J]acks are worth 10 points.
            [A]ces are 1 or 11, player's choice.
            Cards 2 thru 10 are face value.
            (H)it to take another card.
            (S)tand to stop taking cards.
            (D)ouble down to double your bet on the first turn, but you
            have to hit one more time.
            (Sp)lit if you have two cards of equal value on first draw, bet is same on both hands.
            If there is a tie, the bet returns to the player.
            Dealer stands at 17.
            (Q)uit will end the game.""")
    
    money = 1000
    while True: #game loop
        #check if player ran out of money
        if money <= 0:
            print("Oh no! You've run out of money!")
            time.sleep(0.7)
            print("Good thing this wasn't real money.")
            time.sleep(0.7)
            print("Would you like to start over? Y or N")
            if input('> ').upper() == 'Y':
                money = 1000
            else:
                print("Thanks for playing!")
                time.sleep(1)
                gamenight_main()

        #let player enter bet
        print('You have ${}'.format(money))
        bet = getBet(money, gamenight_main)

        #give the dealer and player two cards each from the deck
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        #handle player actions
        print('Bet: ${}'.format(bet))
        while True: #loops until player stands or busts
            displayHands(playerHand, dealerHand, False)
            print()

#checks for blackjack for player, dealer, or both
            if (getHandValue(playerHand) == 21 and len(playerHand) == 2) and (getHandValue(dealerHand) != 21 and len(dealerHand) == 2):
                print('You got Blackjack! \nYou win ${}!'.format(bet * 1.5))
                money += (bet * 1.5)
                break
            elif (getHandValue(playerHand) == 21 and len(playerHand) == 2) and (len(dealerHand) == 2 and getHandValue(dealerHand) == 21):
                print('Blackjack push. Bet is returned.')
                money += bet
                break
            elif (getHandValue(dealerHand) == 21 and len(dealerHand) == 2) and (len(playerHand) == 2 and getHandValue(playerHand) != 21):
                print('House has Blackjack! \nHouse wins ${}!'.format(bet))
                money -= bet
                break

            #check if player bust
            if getHandValue(playerHand) > 21:
                break

            #get player's choice (H,S,D)
            move = getMove(playerHand, money - bet, gamenight_main)

            #handle player's choice
            if move == 'D':
                #double down
                if money >= bet * 2:
                    bet *= 2
                    print('Doubling down! \nBet increased to ${}.'.format(bet))
                    print('Bet: ${}'.format(bet))
                    time.sleep(1)
                else:
                    move.remove('D')

            if move == 'SP':
                #split
                if money >= bet * 2:
                    bet *= 2
                    print('Splitting! \nBet increased to ${}.'.format(bet))
                    print('Bet: ${}'.format(bet))
                    time.sleep(1)
                    handOne = [playerHand[0], deck.pop()]
                    handTwo = [playerHand[1], deck.pop()]
                    print("\n" + "="*40)
                    print("Your hands after splitting:")
                    print("="*40)

                    for i, hand in enumerate([handOne, handTwo], 1):
                        print(f"\nHand {i}:")
                        print("-"*20)
                        displayCards(hand)
                        print(f"Hand {i} Value: {getHandValue(hand)}")
                        print("-"*20)

                    time.sleep(1)

                    for i, hand in enumerate([handOne, handTwo], 1):
                        print(f"\n{'='*20} Playing Hand {i} {'='*20}")

                        while True:
                            print(f"\nCurrent Hand {i}:")
                            displayCards(hand)
                            print(f"Hand {i} Value: {getHandValue(hand)}")
                            displayCards(hand)

                            if getHandValue(handOne) > 21:
                                print('Bust! \nHouse wins ${}!'.format(bet/2))
                                handOne = []
                                break
                            elif getHandValue(handTwo) > 21:
                                print('Bust! \nHouse wins ${}!'.format(bet/2))
                                handTwo = []
                                break
                            move = getMove(hand, money - bet, gamenight_main)
                            
                            if move == 'H':
                                newCard = deck.pop()
                                rank, suit = newCard
                                print('You drew a {} of {}.'.format(rank, suit))
                                hand.append(newCard)
                                time.sleep(1)
                                if getHandValue(handOne) > 21:
                                    print('Bust! \nHouse wins ${}!'.format(bet/2))
                                    handTwo = []
                                    break
                                elif getHandValue(handTwo) > 21:
                                    print('Bust! \nHouse wins ${}!'.format(bet/2))
                                    handTwo = []
                                    break
                                move = getMove(hand, money - bet, gamenight_main)
                            elif move == 'S':
                                break
                            elif move == 'D':
                                if money >= bet * 2:
                                    bet *= 2
                                    print('Doubling down! \nBet increased to ${}.'.format(bet))
                                    print('Bet: ${}'.format(bet))
                                    newCard = deck.pop()
                                    rank, suit = newCard
                                    print('You drew a {} of {}.'.format(rank, suit))
                                    hand.append(newCard)
                                    time.sleep(1)
                                    break
                                else:
                                    print("Not enough money to double down.")
                                    move.remove('D')  
                else:
                    move.remove('Sp')

            if move in ('H', 'D'):
                #hit/doubling takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank,suit))
                time.sleep(1)
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    #player busts
                    continue

            if move in ('S', 'D'):
                #standing/doubling stops player turn
                break

        #handle dealer's actions
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                #dealer hits
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
                print('Dealer hits.')
                time.sleep(1)

                if getHandValue(dealerHand) > 21:
                    break #dealer busts
                input('Press Enter to continue...')
                print('\n\n')

# Show dealer's final hand
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        #handle win, lose, or draw
        if dealerValue > 21:
            print('Dealer busts! \nYou win ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost! \nHouse wins ${}!'.format(bet))
            money -= bet
        elif playerValue > dealerValue:
            print('House loses! \nYou win ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print("It's a push. \nYour bet is returned.")

        input('Press Enter to continue...')
        print('\n\n')

def getBet(maxBet, gamenight_main):
    """Ask how much the player wants to bet, and make sure it's valid."""
    while True: #asks until a valid amount is input
        print('How much would you like to bet? (1-{}), (A)ll in, or (Q)uit.'.format(maxBet))
        bet = input('>> ').upper().strip()
        if bet == 'A':
            return maxBet
        if bet == 'Q':
            print('Come back again soon!')
            time.sleep(1)
            gamenight_main()
        
        if not bet.isdecimal():
            continue #player didn't enter a number so ask again

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet #valid bet
        
def getDeck():
    """Returns list of (rank,suit) tuples for 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range (2,11):
            deck.append((str(rank), suit)) #add numbered cards
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) #add face cards
    random.shuffle(deck) #shuffles cards
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    """Shows hands but hides dealer's first card if showDealerHand is False."""
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        #hides dealer's first card
        displayCards([BACKSIDE] + dealerHand[1:])
    
    #show player cards
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    """Returns the value of the cards in the hand. Since Aces are 1 or 11
    it picks most suitable value."""
    value = 0
    numberOfAces = 0

    #add non-ace cards
    for card in cards:
        rank = card[0] #card is tuple
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('J', 'Q', 'K'):
            value += 10
        else:
            value += int(rank) #numbered card value
    
    #Add value for aces
    value += numberOfAces #1 per ace
    for i in range(numberOfAces):
        #if another 10 can be added without busting, it will
        if value + 10 <= 21:
            value += 10 #add 10 to value
        
    return value

def displayCards(cards):
    """Displays cards in list"""
    rows = ['', '', '', '', '', ''] #top row, middle row, etc

    for i, card in enumerate(cards):
        rows[0] += '  _____ '
        if card == BACKSIDE:
            rows[1] += ' |     |'
            rows[2] += ' | ~ ~ |'
            rows[3] += ' |     |'
            rows[4] += '  ----- '
            rows[5] += ' '
        else:
            rank, suit = card
            rows[1] += ' |{}    |'.format(rank.ljust(1))
            rows[2] += ' |  {}  |'.format(suit)
            rows[3] += ' |    {}|'.format(rank.rjust(1))
            rows[4] += '  ----- '
            rows[5] += ' '
    for row in rows:
        print(row)

def getMove(playerHand, money, gamenight_main):
    """Asks for player's move and makes sure it's valid."""
    while True: #ask til player enters valid move
        moves = ['(H)it, (S)tand', '(Q)uit']
        """Player can double on first move because they have 2 cards"""
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        if len(playerHand) == 2 and money > 0 and (playerHand[0][0] == playerHand[1][0] or (playerHand[0][0] in '10JQK' and playerHand[1][0] in '10JQK')):
            moves.append('(Sp)lit') #allow a split if the cards are the same
        #get player's move
        movePrompt = ', '.join(moves) + ' >> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move #valid move
        if move == 'D' and '(D)ouble down' in moves:
            return move #valid move
        if move == 'SP' and '(Sp)lit' in moves:
            return move #valid move
        if move == 'Q':
            print('Thanks for playing!')
            time.sleep(1)
            gamenight_main()

if __name__ == '__main__':
    main(gamenight_main)