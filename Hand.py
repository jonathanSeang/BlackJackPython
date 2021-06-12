# Represents a hand dealt in BlackJack

class Hand:

    def __init__(self, alias, cards):
        self.alias = alias
        self.cards = cards
        self.possible_values = []

        # add case where 'Ace' is valued as 11
        for card in cards:
            curr_value = 0
            curr_value += card.value
        self.possible_values.append(curr_value)

        # for every card, subtract value by 10 and append to list
        VALUE_SUBTRACTED_PER_ACE = 10
        for card in cards:
            curr_value = self.possible_values[0] # start at max value and decrement for every 'Ace'
            if card.rank == 'Ace':
                curr_value -= VALUE_SUBTRACTED_PER_ACE
                self.possible_values.append(curr_value)

    def __str__(self):
        return self.alias + " current cards are " + self.cards

    def check_hand_busts(self):
        pass
