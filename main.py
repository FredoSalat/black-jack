# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import typing

import dealer_class
import deck_class
import player_class

suits = ('Hearts', 'Diamonds', 'Spades',
         'Clubs')  # A tuple that holds the four values of a card deck Tuple is used since they are immutable and
# these values should stay the same
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King',
         'Ace')  # A tuple that holds the value of each card. Tuple is used since they are immutable and these
# values should stay the same
values: dict[typing.Union[str, typing.Any], typing.Union[int, typing.Any]] = {'Two': 2, 'Three': 3, 'Four': 4,
                                                                              'Five': 5, 'Six': 6, 'Seven': 7,
                                                                              'Eight': 8,
                                                                              'Nine': 9, 'Ten': 10, 'Jack': 10,
                                                                              'Queen': 10, 'King': 10, 'Ace': 11}

# Fixa med clear output (kolla tictactoe)


# Multiple players: behöver en loop med variabel för varje spelare


# ----------

list_of_entities = []


def players_at_table():
    list_of_players = []  # Empty list of players that will later be returned
    player_count = 1  # Counter to help the user keep track of which player should be named what
    num_of_players = int(input("How many players are you?"))  # Asks the user how many people ought to play at the table
    for num in range(num_of_players):  # Loop running through the amount of players entered above
        player_at_table = player_class.Player()  # Creating a new instance of a player
        print(f"Enter the name of player {player_count}")  # Asks the user for the name of the player
        player_count += 1
        player_at_table.set_name()  # Calls the set-name method to allow the user to enter their own name
        list_of_players.append(player_at_table)  # appends the user to the list of players
        list_of_entities.append(player_at_table)
    return list_of_players


def dealer_win_check():
    pass


if __name__ == '__main__':
    # Setting up the basics of the game - deck, instance of a dealer, number of players and finishing by
    # establishing a while-loop to run until no further hands should be played

    # the deck variable holds a shuffled version of a new deck that is created everytime a new game is created
    deck = deck_class.Deck()
    deck.shuffle()

    # Created an instance of a dealer, which is currently coming from the parent-class EntityAtTable
    dealer = dealer_class.Dealer()
    list_of_entities.append(dealer)

    # creates a list of the number of players added as an integer by the user and allows the user to add the name of
    # each player
    players = players_at_table()

    playing_hand = True

    # Most outer while-loop within a hand that controls the must-haves of each round (two cards for each player and
    # the dealer)
    while playing_hand:
        players_left_in_round = []

        # Loops through the players and resets their bet and total count for every hand before asking them for the
        # bet of the current round
        for player in players:
            player.bet = 0
            player.total_count = 0
            player.bet = player.place_bet()
            players_left_in_round.append(player)

        # Loops through a list of all entities (players and dealer)
        for entity in list_of_entities:
            entity.hit(deck.deal())
            entity.hit(deck.deal())
            # calls the hit method which belongs to the parent-class entityattable and
            # appends two cards
            entity.display_cards()  # calls the display_card method which is unique to the player and dealer,
            # since the dealer only can show one of the cards on hand

        dealer_hit = False
        player_hitting = True

        for player in players:

            # Inner while-loop running as many laps as the player wants to hit
            while player_hitting:

                player.ace_checker()  # beginning to check for any aces on hand and adjusting the count according to it

                print(f'{player.name} your total count is {player.total_count}')  # Presenting the total count of the
                # player

                if player.bust_checker():  # Checking if the player is over 21
                    print(f'{player.name} you are bust')  # Informing the player of being bust
                    player.balance = player.balance_withdraw()  # Adjusts the balance and removes the player if the balance is equal to zero
                    del players_left_in_round[player]
                    if player == players[-1]:
                        dealer_hit = True
                        player_hitting = False
                        break
                    else:
                        continue

                else:
                    answer = int(input("Press 1 to get another card. Press 2 to pass"))

                if answer == 1:
                    player.hit(deck.deal())
                    player.display_cards()
                    continue

                elif answer == 2:
                    if player == players[-1]:
                        dealer_hit = True
                        player_hitting = False
                    else:
                        break

        while dealer_hit:

            dealer.ace_checker()

            if dealer.bust_checker():
                for player in players_left_in_round:
                    print(f'{player.name} you won this round')
                    player.balance_insert()
                    dealer_hit = False
                    break

            for player in players_left_in_round:
                if dealer.total_count > player.total_count:
                    print(
                        f'{player.name} you lost this round. Your count was {player.total_count} and the dealer was {dealer.total_count}')
                    player.balance_withdraw()
                    dealer_hit_me = False
                    break

            for player in players_left_in_round:
                if dealer.total_count < player.total_count:
                    dealer.get_card(deck.deal())
                    continue
