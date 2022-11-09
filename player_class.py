# This is the child class of the EntityAtTable class (in lack of better name)
# When instantiated, this object also comes with its parent, which shares attributes with the dealer

from entity_at_table_class import EntityAtTable


class Player(EntityAtTable):

    def __init__(self):
        EntityAtTable.__init__(self)  # calling the init function of the superclass (entityattable)
        self.bet = 0
        self.name = ''
        self.balance = 4000

    def set_name(self):
        self.name = str(input())

    def place_bet(self):
        while True:
            try:
                self.bet = int(input(
                    f"{self.name} how much do you want to bet this round? Your current balance is {self.balance}"))
            except ValueError:
                print("Please enter a valid integer")
            else:
                if 0 < self.bet <= self.balance:
                    break
                else:
                    print(f"Please enter a bet larger than 0 and less than {self.balance}")

        return self.bet

    def display_cards(self):
        print(f"{self.name}, these are the cards you currently have on hand: ")
        for card in self.cards_on_hand:
            print(card)

    def balance_withdraw(self):
        self.balance = self.balance - self.bet
        if self.balance <= 0:
            print(f"{self.name} you have no balance, you have been removed from the table.")
            del self
        else:
            return self.balance

    def balance_insert(self):
        self.balance += self.bet * 2

    def win_check(self):
        pass

    def __str__(self):
        return self.name
