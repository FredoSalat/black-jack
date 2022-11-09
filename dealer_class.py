# Dealer - class
from entity_at_table_class import EntityAtTable


class Dealer(EntityAtTable):

    def __init__(self):
        EntityAtTable.__init__(self) # calling the init function of the superclass (entityattable)
        self.name = 'Dealer'

    def display_cards(self):
        print(f"The dealer have {len(self.cards_on_hand)} cards on hand. This is the first open one: {self.cards_on_hand[0]} ")