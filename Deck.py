import random
import Card

# Represents an entire deck with 52 unique cards

class Deck:

    def __init__(self):
        self.card_list = []

        suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        for rank in ranks:
            for suit in suits:
                self.card_list.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.card_list)

    def deal_n_cards(self, n):
        dealt_cards = []
        for i in range(0, n):
            dealt_cards.append((self.card_list.pop(0)))
        return dealt_cards
