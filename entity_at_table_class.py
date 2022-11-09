# The parent class of player, which contains the attributes of both the player and dealer


class EntityAtTable:

    def __init__(self):
        self.cards_on_hand = []
        self.total_count = 0
        self.ace_counter = 0

    def hit(self, new_card):
        import main
        self.cards_on_hand.append(new_card)
        self.total_count += main.values[new_card.rank]
        if new_card.rank == 'Ace':
            self.ace_counter += 1

    def ace_checker(self):
        while self.total_count > 21 and self.ace_counter:
            self.total_count -= 10
            self.ace_counter -= 1

    def bust_checker(self):
        if self.total_count > 21:
            return True
        if self.total_count < 21:
            return False
