import random

import card_class
import main


class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in main.suits:
            for rank in main.ranks:
                self.all_cards.append(card_class.Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
       return self.all_cards.pop(0)

