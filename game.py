import cards
import random
import collections


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.cards.pop())
        return self

    def drop(self, hand, card_pool):
        # The user will enter the index of the card they want to drop
        """
        from their hand we need to find the exact card value that means
         listing the cards out for the user so that they an specifically
         choose an index of the card they wish to discard from their hand
          and remove it then send that card to the pool.

          This part could use more thinking...
          am not sure what I just did but am hopping it works
        """

        self.show_hand()
        index = int(input("Enter the card value you want to drop! "))
        card_index = index - 1
        dropped_card = self.hand.pop(card_index)
        card_pool.append(dropped_card)
        return card_pool

    def show_hand(self):
        index = 1
        for card in self.hand:
            print(f"{index}.) ", end="")
            index += 1
            print(card)
            # card.display()

    def __str__(self):
        return f'{self.name} =>> {self.hand}'


class Game:
    def __init__(self):
        pass

    # Initialize Game players, number of players and names.
    def game_players(self):
        # initialize the number of players, their names and their hands.
        # numbers of players is variable. max number will be 5 players
        number_of_players = int(input("Enter the number of player: "))
        players_list = []
        for i in range(number_of_players):  # Initialising a list of players
            # Instantiate player objects and initialise their hands
            players_list.append(Player(input(f"Enter Player {i + 1}'s name: ")))
        return players_list

    def check_win(self, hand):

        for card in range(len(hand)):
            if hand[card].value in hand:
                return hand[card]

    def play(self, player, deck):
        player.draw(deck)
        game_over = check_winner(player, player.hand)

        if not game_over:
            next_player()
            # We may need to check if the deck is still having cards

    pass


def next_player(players_list, current_player):
    for i in range(len(players_list)):
        if players_list[i] == current_player:
            Game.play(players_list[i + 1], deck)


def check_winner(player, hand, card_pool):
    current_player = player

    card_values = []
    card_values_set = set()

    duplicate_card_values = None
    duplicate_value = None
    duplicate_pair_1 = None
    duplicate_pair_2 = None
    duplicate_cards = []
    matching_pair = False
    sequential_pair = False

    unique_card_values = None
    unique_cards = None
    sequential_cards = []

    winning_cards = []

    for card in range(len(hand)):
        # makes a list of the values for each card
        card_values.append(hand[card].value)

    # check the list for duplicate card values and returns a list
    duplicate_card_values = check_for_duplicates(card_values)

    if duplicate_card_values:  # checks if there is any duplicate card values
        # for duplicate card value we card find the cards with
        for i in range(len(duplicate_card_values)):
            duplicate_value = duplicate_card_values[i]

        card_values_set = set(card_values)
        card_values_set.remove(duplicate_value)
        unique_card_values = list(card_values_set)

        # Finds the duplicate card values and appends them to a new list
        for card in range(len(hand)):
            if hand[card].value == duplicate_value:
                duplicate_cards.append(hand[card])
                matching_pair = True
        print("The duplicate cards are: ", end="")
        print(duplicate_cards)

    # This is for cases when a player has two pairs of duplicate cards
    elif len(duplicate_card_values) > 1:
        print("There are two duplicate card values")
        for value in range(len(duplicate_card_values) - 1):
            # User may need to be asked what pair they want to use.
            duplicate_pair_1 = duplicate_card_values[value]
            duplicate_pair_2 = duplicate_card_values[value + 1]
            matching_pair = True
        print(f"Pair 1: {duplicate_pair_1}")
        print(f"Pair 2: {duplicate_pair_2}")

    # If No duplicates found then there is no chance of winning
    else:
        # player must choose a card to drop
        # after player has dropped a card into the pool, next player can draw
        print(f"ALL CARDS ARE UNIQ CARDS = {current_player.hand}")
        print("You must drop a card for the next player to go!")
        card_pool = current_player.drop(current_player.hand, card_pool)
        print(f"{current_player.name} dropped {card_pool[-1]}")
        return card_pool, current_player
        # next_player(current_player)
        # Now go to next_player()

    if matching_pair:
        print(f" IF MATCHING PAIR EXISTS THEN UNIQ = {unique_card_values} \n")
        # Bool - Checks for consecutive numbers for the cards - Returns True or False
        sequential_pair = check_for_sequence(unique_card_values)

        if sequential_pair:
            for card in range(len(unique_card_values)):
                if hand[card].value == unique_card_values[card]:
                    sequential_cards.append(hand[card])
            print(sequential_cards)

        else:
            print("Player must choose a card to drop")

    if matching_pair and sequential_pair:
        print(f"GAME OVER!!! {current_player.name} WINS!!! \n")


def check_for_duplicates(card_value_list):
    occurrences = []
    for item in card_value_list:
        count = 0
        for x in card_value_list:
            if x == item:
                count += 1
        occurrences.append(count)

    duplicates = set()
    index = 0
    while index < len(card_value_list):
        if occurrences[index] != 1:
            duplicates.add(card_value_list[index])
        index += 1

    return list(duplicates)


def check_for_sequence(unique_card_values):
    sequence_pair = False

    sorted_list = sorted(unique_card_values)
    # sorted(l) ==
    range_list = list(range(min(unique_card_values), max(unique_card_values) + 1))
    if sorted_list == range_list:
        print("There are consecutive numbers")
        sequence_pair = True
        return sequence_pair
    else:
        print("There are no consecutive numbers")
        sequence_pair = False
        return sequence_pair


# The unwanted cards will be thrown down into the pool
card_pool = []

deck = cards.Deck()
deck.shuffle()

bob = Player('Bob')
didi = Player('didi')
players = [bob, didi]
deck.deal(players)

print(bob)
bob.draw(deck)
print(bob)
check_winner(bob, bob.hand, card_pool)
print(card_pool)
print(bob)

