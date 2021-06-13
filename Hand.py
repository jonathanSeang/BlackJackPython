# Represents a hand dealt in BlackJack

class Hand:

    def __init__(self, alias, cards):
        self.alias = alias  # Name of Hand owner- usually either Dealer or Player
        self.cards = cards
        self.possible_values = []  # All possible values that can be created using this Hand
        self.update_values()

    # update all possible values whenever new card is put in
    def add_cards(self, cards):
        self.cards.extend(cards)
        self.update_values()

    def update_values(self):
        new_values = []
        curr_value = 0
        for card in self.cards:
            curr_value += card.value
            # print(f"new curr_value: {curr_value} after adding {str(card)} with value of {card.value}")
        new_values.append(curr_value)

        # for every card, if there is an 'Ace' subtract value by 10 and append to list
        VALUE_SUBTRACTED_PER_ACE = 10
        for card in self.cards:
            curr_value = new_values[0]  # start at max value and decrement for every 'Ace'
            if card.rank == 'Ace':
                curr_value -= VALUE_SUBTRACTED_PER_ACE
                new_values.append(curr_value)

        self.possible_values = new_values

    def __str__(self):
        return str(self.alias) + " current cards are " + ', '.join(map(str, self.cards))

    def check_if_hand_busts(self):
        # because cards are sorted from greatest to least, we can check if the lowest value has bust
        return self.possible_values[len(self.possible_values)-1] > 21
