# BlackJack Project
# Will have a dealer and human player
# Uses a normal deck of cards
# Player has limited amount of cash
# Player can HIT or STAY to get to 21
#     Maybe add INSURANCE, SPLIT, or DOUBLE DOWN
# If player under 21, deal hits until they beat player or dealer busts

from Deck import Deck
from Hand import Hand

STARTING_NUMBER_OF_CHIPS = 100
CARDS_DEALT_AT_START = 2
CARDS_DEALT_PER_HIT = 1


# prints current chips available and asks for amount to be bet
def ask_for_bet(chips_available):
    print("\n\n\nYou currently have " + str(chips_available) + " chips available")

    while (True):
        try:
            bet_amount = int(input("Please input the amount you would like to bet: "))
            if bet_amount > chips_available: raise Exception
        except:
            print("Value is invalid")
        else:
            break

    return bet_amount


def ask_for_hit(player_hand):
    print("\nCurrent hand value is " + str(player_hand.possible_values))

    while True:
        player_input = input("Would you like to HIT? (Type 'Hit' to Hit and 'Stand' to Stand) ")

        if player_input == 'Hit':
            return True
        elif player_input == 'Stand':
            return False
        else:
            continue


# Whenever new card is added, throw this exception so we can restart function
class ContinueDueToNewCard(Exception):
    pass


# Dealer will always Hit until dealer's value meets or exceeds 17
def dealer_action(deck, dealer_hand):
    # For every possible value, check if any of them are in range(17, 21)
    while True:  # Loop used to restart possible_values
        try:
            for value in dealer_hand.possible_values:
                while value < 17:
                    new_card = deck.deal_n_cards(CARDS_DEALT_PER_HIT)
                    dealer_hand.add_cards(new_card)
                    raise ContinueDueToNewCard  # Break out while loop whenever new card is added
            break
        except ContinueDueToNewCard:
            continue

    if dealer_hand.check_if_hand_busts():
        print("Dealer hand busts!")

    print("\nDealer hand value is " + str(dealer_hand.possible_values))


def find_if_player_won(dealer_hand, player_hand):
    dealer_highest = 0
    for value in dealer_hand.possible_values:
        if value <= 21:
            dealer_highest = value
            break

    player_highest = 0
    for value in player_hand.possible_values:
        if value <= 21:
            player_highest = value
            break

    return player_highest > dealer_highest


def ask_to_continue():
    while True:
        player_input = input("Would you like to continue playing? (Type 'Continue' to Continue and 'Quit' to Quit ")

        if player_input == 'Continue':
            return True
        elif player_input == 'Quit':
            return False
        else:
            continue


if __name__ == '__main__':

    chips_available = STARTING_NUMBER_OF_CHIPS
    game_in_play = True

    while game_in_play:

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
        while hand_in_play:

            # ask if want to hit or stay
            hand_in_play = ask_for_hit(player_hand)

            if hand_in_play:  # deal player a card if hit
                new_cards = deck.deal_n_cards(CARDS_DEALT_PER_HIT)
                print("Dealer has given you " + ', '.join(map(str, new_cards)))
                player_hand.add_cards(new_cards)

                # check if bust else ask to hit
                if player_hand.check_if_hand_busts():
                    print("Your hand busts!")
                    hand_in_play = False

        # if player stands, dealer action
        dealer_action(deck, dealer_hand)
        print(dealer_hand)

        # determine winner and adjust chips
        if find_if_player_won(dealer_hand, player_hand):
            chips_available += chips_bet
            print(f"\nCongratulations! You won {chips_bet} with a new total of {chips_available}")
        else:
            chips_available -= chips_bet
            print(f"\nSorry. You lost {chips_bet} with a new total of {chips_available}")

        # ask player to play again
        game_in_play = ask_to_continue()

    print(f"\n\nYou finished with a total of {chips_available}")
