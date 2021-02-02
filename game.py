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

    def drop(self, hand, pool):
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
        pool.append(dropped_card)
        return self, pool

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


def check_winner(player, hand):
    duplicate_pair_1 = None
    duplicate_pair_2 = None
    matching_pair = False
    current_player = player
    card_values = []
    card_values_set = set()
    duplicate_value = None
    duplicate_card_values = None
    duplicate_cards = []
    sequential_cards = []
    winning_cards = []

    for card in range(len(hand)):
        # makes a list of the values for each card
        card_values.append(hand[card].value)

    # check the list for duplicate card values and returns a list
    duplicate_card_values = check_for_duplicates(card_values)

    if duplicate_card_values: # checks if there is any duplicate card values
        # for duplicate card value we card find the cards with
        for i in range(len(duplicate_card_values)):
            duplicate_value = duplicate_card_values[i]

        card_values_set = set(card_values)
        card_values_set.remove(duplicate_value)
        unique_card_values = list(card_values_set)

        for card in range(len(hand)):
            if hand[card].value == duplicate_value:
                duplicate_cards.append(hand[card])
                matching_pair = True

        # Here we have our duplicate cards
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
        print(None)
        # player must choose a card to drop
        # after player has dropped a card into the pool, next player can draw


    if matching_pair:
        print(f" IF MACTCHING PAIR THEN UNIQ = {unique_card_values} \n")
        check_for_sequencial()


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


    """
    matching_pair = False
    seq_pair = False
    for card in range(len(hand)):
        card_values.append(hand[card].value)
        card_values_set = set(card_values)
        duplicate_card_value = [card for card, count in collections.Counter(card_values).items() if count > 1]

    if duplicate_card_value != []:
        for card in range(len(duplicate_card_value)):
            duplicate_card_value = duplicate_card_value[card]
            print(duplicate_card_value)

        for card in range(len(hand)):
            if hand[card].value == duplicate_card_value:
                duplicate_cards.append(hand[card])
                matching_pair = True

        print(duplicate_cards[:2])

    else:
        print(None)

    if matching_pair:
        for card in range(len(card_values_set)):
            print(card)
            if card_values_set[card] == duplicate_card_value:
                continue
            else:
                sequential_cards.append(hand[card])
        print(sequential_cards)




    unique = list(set(card_values))
    print(f"UNIQUE VALUES => {unique}")

    for value in range(len(unique)):
        if unique[value] in duplicate_card_value:
            duplicate_card_value = unique[value]
            print(duplicate_card_value)

    for card in range(len(hand)):
        if hand[card].value == duplicate_card_value:
            duplicate_cards.append(hand[card])
            matching_pair = True

    print(duplicate_cards)
    print(hand)



          
    

    if duplicate_card_value in unique:
        unique.remove(duplicate_card_value)
        print("These are the remaining unique cards: ", end="")
        print(unique)

        for card_value in range(len(unique)):
            if hand[card_value].value in unique:
                sequential_cards.append(hand[card_value])

    else:
        print("All values are unique!!")


    print(sequential_cards)





    try: # Try Checking for card duplicates in the player's hand
        for card in range(len(hand)):
            if hand[card].value == duplicate_card_value[0]:
                duplicate_cards.append(hand[card])
                hand.remove(hand[card])
                matching_pair = True

        print(duplicate_cards)
        print(hand)

    except: # If no Matching pairs then player drops one card and game proceeds
        \"""
        Since the player has no matching pair values in their hand,
        there is not chance of winning, so they can drop a card
        so that they remain with 3 cards and the next player can draw.
        
        \"""
        print("No Matching Card values\n")
        print("You need to drop one card for the game to proceed \n")
        # If player does not win, they drop a card of their choice from their hand
        # player.drop(player.hand, pool)

    
    # If player wins then game is over and they show their hand
    game_over = f"GAME OVER!!! - Player {player.name} Has won!!!\n {player}"
    winning_cards = []
"""

def check_for_sequencial():
    pass

# players = Game.game_players()

# The unwanted cards will be thrown down into the pool
card_pool = []

deck = cards.Deck()
deck.shuffle()

bob = Player('Bob')
players = [bob, ]
deck.deal(players)

print(bob)
bob.draw(deck)

bob.show_hand()

check_winner(bob, bob.hand)

# next_player(current_player)
