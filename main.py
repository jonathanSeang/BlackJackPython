# BlackJack Project
# Will have a dealer and human player
# Uses a normal deck of cards
# Player has limited amount of cash
# Player can HIT or STAY to get to 21
#     Maybe add INSURANCE, SPLIT, or DOUBLE DOWN
# If player under 21, deal hits until they beat player or dealer busts

# TODO:
# - Create deck of 52 cards
# - shuffle the deck
# - ask player for their bet
# - make sure player's bet does not exceed available chips
# - deal two cards to the deal and two to player
# - show only one of the dealer's cards, the other remains hidden
# - show both of the player's cards
# - ask the player if to hit
# - if player doesn't bust, ask if the want to hit again
# - if player stands, player the dealer's hand. Deal will always Hit until dealer's value meets or exceeds 17
# - Determine winner and adjust Player's chips
# - Ask player to play again

import Card
import Deck
import Hand

# prints current chips available and asks for amount to be bet
def ask_for_bet(chips_available):
    pass

def ask_for_hit():
    pass

def dealer_action(dealer_hand, player_hand):
    pass

def find_if_player_won(dealer_hand, player_hand):
    pass

def ask_to_continue():
    pass

if __name__ == '__main__':

    STARTING_NUMBER_OF_CHIPS = 100
    chips_available = STARTING_NUMBER_OF_CHIPS
    game_in_play = True

    while(game_in_play):

        CARDS_DEALT_AT_START = 2

        # instantiate deck
        deck = Deck()
        deck.shuffle()

        # ask for bet
        chips_bet = ask_for_bet(chips_available)

        # deal initial cards
        dealer_hand = Hand('Dealer', deck.deal_n_cards(CARDS_DEALT_AT_START))
        player_hand = Hand('Player', deck.deal_n_cards(CARDS_DEALT_AT_START))

        # show appropriate cards
        print("Dealer reveals his first card is: " + str(dealer_hand.cards[0]))
        print(player_hand)

        hand_in_play = True
        while(hand_in_play):

            CARDS_DEALT_PER_HIT = 1

            print("Current hand value is " + player_hand.value)

            # ask if want to hit or stay
            player_hits = ask_for_hit()

            if player_hits: # deal player a card if hit
                player_hand.cards.append(deck.deal_n_cards(CARDS_DEALT_PER_HIT))

            # check if bust else ask to hit
            if player_hand.check_hand_busts():
                hand_in_play = False


        # if player stands, dealer action
        dealer_action(dealer_hand, player_hand)
        print(dealer_hand)

        # determine winner and adjust chips
        if find_if_player_won(dealer_hand, player_hand):
            print("Congratulations! You won " + chips_bet)
            chips_available += chips_bet
        else:
            print("Sorry. You lost " + chips_bet)
            chips_available -= chips_bet

        # ask player to play again
        game_in_play = ask_to_continue()

    print("You finished with a total of " + chips_available)
