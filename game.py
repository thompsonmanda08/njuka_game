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
        try:
            index = int(input("Enter the card value you want to drop! "))
            card_index = index - 1
            dropped_card = self.hand.pop(card_index)
            card_pool.append(dropped_card)
        except:
            print("You only have 4 cards in your hand, choose numbers from 1 to 4 to pick a card!")

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
    sorted_list = sorted(unique_card_values)
    range_list = list(range(min(unique_card_values), max(unique_card_values) + 1))

    if sorted_list == range_list:
        print("CONSECUTIVE NUMBERS EXIST!")
        return True
    else:
        print("NO CONSECUTIVE NUMBERS!")
        return False


# Checks for the winner
def check_winner(players_list, hand, card_pool):
    """
    Checks for the winner of the game
    :param players:
    :param players list:
    :param current player hand list:
    :param card_pool:
    :return: True if player wins the game.
    """

    current_player = None
    for player in range(len(players_list)):
        if players_list[player].hand == hand:
            current_player = players_list[player]
    print(f"CURRENT PLAYER = {current_player}")

    card_values = []
    card_values_set = set()

    duplicate_card_values = []
    duplicate_value = None
    duplicate_pair_1 = None
    duplicate_pair_2 = None
    duplicate_cards = []
    matching_pair = False

    unique_card_values = None
    unique_cards = []
    sequential_cards = []
    sequential_pair = False

    winning_cards = []
    winner = False

    for card in range(len(hand)):
        # makes a list of the values for each card
        card_values.append(hand[card].value)

    # check the list of card values for duplicates and returns a list of the duplicates
    duplicate_card_values = check_for_duplicates(card_values)

    if len(duplicate_card_values) == 1:  # checks if there is any duplicate card values
        # for duplicate card value we card find the cards with
        duplicate_value = duplicate_card_values[0]

        card_values_set = set(card_values)
        # filters out the duplicate values with a set leaving only unique values
        # however one of the cards is a duplicate value

        if len(card_values_set) == 3:  # This means there is one pair of duplicates
            card_values_set.remove(duplicate_value)  # removes the duplicate value from set
            unique_card_values = list(card_values_set)  # makes a list of the unique values after removing the duplicate

        elif len(card_values_set) == 2:

            """
             By running the above code there is chance that the dupplicate value appears 3 times
             and so there is still a bug, because by removing the duplicate value all 3 cards that
             are supposedly the same will be removed.

             It so happens that the set() function will remove that value as well and then
             we end up with only one unique value which is not the case.
             We will look into this later!!!
            
            This means there one duplicate pair and a loose value or
            there could be 2 pairs of duplicate
            
            So lets deal with these one by one.
            """
            # Assuming there are two pairs of duplicates:

            print("There are more than 2 identical card values")
            print(f"CARD VALUE SET = {card_values_set}")

        # Finds the duplicate card values and appends them to a new list
        for card in range(len(hand)):
            if hand[card].value == duplicate_value:
                duplicate_cards.append(hand[card])

            if len(duplicate_cards) == 2:
                matching_pair = True
                break

    # This is for cases when a player has two pairs of duplicate cards
    elif len(duplicate_card_values) == 2:
        print("There are two duplicate card values")
        for value in range(len(duplicate_card_values) - 1):
            # User may need to be asked what pair they want to use.
            duplicate_pair_1 = duplicate_card_values[value]
            duplicate_pair_2 = duplicate_card_values[value + 1]

            """
            Now that we have the duplicate pair values we can extract each of these
            cards from the players hands and ask the player which pair they would like
            to keep.
            
            After choosing to keep one pair... the other pair is dropped into the card pool
            and the player can draw one more extra card to make their hand
            complete so that the game can proceed to the next player.
            
            On the on other hand the player may not want to tell their opponent that they have
            2 pairs of duplicates and in this case the player will want to drop one card and then
            continue playing their strategy
            
            """

            matching_pair = True
        print(f"Pair 1: {duplicate_pair_1}")
        print(f"Pair 2: {duplicate_pair_2}")

    # If No duplicates found then there is no chance of winning next player must go!
    else:
        # player must choose a card to drop
        # after player has dropped a card into the pool, next player can draw
        print(f"ALL CARDS ARE UNIQ CARDS = {current_player.hand}")
        print("You must drop a card for the next player to go!")
        while not card_pool:
            card_pool = current_player.drop(current_player.hand, card_pool)
            if card_pool:
                print(f"{current_player.name} dropped {card_pool[-1]}")
                return card_pool, current_player

        # Now go to next_player()

    if matching_pair:
        print(f"IF DUPLICATE CARDS = {duplicate_cards}")
        for card in range(len(hand)):
            if hand[card].value not in duplicate_card_values:
                unique_cards.append(current_player.hand[card])
        print(f"THEN UNIQUE CARDS = {unique_cards}")

        # Bool - Checks for consecutive numbers for the cards - Returns True or False
        sequential_pair = check_for_sequence(unique_card_values)
        if sequential_pair:
            sequential_cards = unique_cards

        else:
            print("Close but No cigar! You must drop a card for the next player to go!")
            card_pool = current_player.drop(current_player.hand, card_pool)
            print(f"{current_player.name} dropped {card_pool[-1]}")
            print(f"{current_player}")
            return card_pool, current_player

    if matching_pair and sequential_pair:
        print(f"GAME OVER!!! {current_player.name} WINS!!!")
        winning_cards.extend(duplicate_cards)
        winning_cards.extend(sequential_cards)
        print(f"WINNING CARDS = {winning_cards}")


# Initialize Game players, number of players and names.
def game_players():
    # initialize the number of players, their names and their hands.
    # numbers of players is variable. max number will be 5 players
    number_of_players = int(input("Enter the number of player: "))
    players_list = []
    for i in range(number_of_players):  # Initialising a list of players
        # Instantiate player objects and initialise their hands
        players_list.append(Player(input(f"Enter Player {i + 1}'s name: ")))
    return players_list


# move to the next play
def next_player(current_player, deck):
    pass


# The unwanted cards will be thrown down into the pool
card_pool = []

deck = cards.Deck()
deck.shuffle()

bob = Player('Bob')
didi = Player('didi')
players = [bob, didi]
deck.deal(players)

bob.draw(deck)
check_winner(players, bob.hand, card_pool)
# print(f"Card at the top of the pool is {card_pool}")


class Game:
    def __init__(self):
        pass

    def play(self, player, deck):
        player.draw(deck)
        game_over = check_winner(player, player.hand)

        if not game_over:
            next_player()
            # We may need to check if the deck is still having cards
