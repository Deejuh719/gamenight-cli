import random, sys, time

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
            have to hit one more time before you can stand.
            If there is a tie, the bet returns to the player.
            Dealer stands at 17.
            (Q)uit will end the game.""")
    
    money = 1000
    while True: #game loop
        #check if player ran out of money
        if money <= 0:
            print("Oh no! You've run out of money!")
            time.sleep(0.5)
            print("Good thing this wasn't real money.")
            time.sleep(0.5)
            print("Thank you for playing!")
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

            #check if player bust
            if getHandValue(playerHand) > 21:
                break

            #get player's choice (H,S,D)
            move = getMove(playerHand, money - bet)

            #handle player's choice
            if move == 'D':
                #double down
                additionalBet = getBet(min(bet, (money-bet)))
                bet += additionalBet
                print('Bet increased to ${}.'.format(bet))
                print('Bet: ${}'.format(bet))
                
            if move in ('H', 'D'):
                #hit/doubling takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank,suit))
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
                print('Dealer hits.')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break #dealer busts
                input('Press Enter to continue...')
                print('\n\n')

        #show dealer's final hand
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        #handle win, lose, or draw
        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You win ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print("It's a push. Your bet is returned.")

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
    rows = ['', '', '', '', ''] #top row, middle row, etc

    for i, card in enumerate(cards):
        rows[0] += '  _____ '
        if card == BACKSIDE:
            rows[1] +=' | ~ ~ | '
            rows[2] +=' | ~ ~ | '
            rows[3] +=' | ~ ~ | '
            rows[4] +='  ------ '
        else:
            rank, suit = card #card is tuple
            rows[1] +=' |{} {} {}| '.format(rank, suit, suit)
            rows[2] +=' |{} {} {}| '.format(suit, rank, suit)
            rows[3] +=' |{} {} {}| '.format(suit, suit, rank)
            rows[4] +='  ------ '

    for row in rows:
        print(row)

def getMove(playerHand, money, gamenight_main):
    """Asks for player's move and makes sure it's valid."""
    while True: #ask til player enters valid move
        moves = ['(H)it, (S)tand', '(Q)uit']
        """Player can double on first move because they have 2 cards"""
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        
        #get player's move
        movePrompt = ', '.join(moves) + ' >> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move #valid move
        if move == 'D' and '(D)ouble down' in moves:
            return move #valid move
        if move == 'Q':
            print('Thanks for playing!')
            time.sleep(1)
            gamenight_main()

if __name__ == '__main__':
    main()