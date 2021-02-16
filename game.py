import cards
import random
import collections
import time


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        assert len(self.hand) <= 4
        try:
            new_card = deck.cards.pop()
            self.hand.append(new_card)
        except:
            print("Error: The Deck is empty!")
        return self

    def drop(self, hand):
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
            index = int(input("\nEnter the card value you want to drop! "))
            card_index = index - 1
            drop = self.hand.pop(card_index)
            return drop

        except:
            drop_error = "You only have 4 cards in your hand, choose numbers from 1 to 4 to pick a card!"
            return drop_error

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
    
    try:
        sorted_list = sorted(unique_card_values)
        range_list = list(range(min(unique_card_values), max(unique_card_values) + 1))
    except TypeError:
        print("type error is occuring here!!!")

    if sorted_list == range_list:
        print("CONSECUTIVE NUMBERS EXIST!")
        return True
    else:
        print("NO CONSECUTIVE NUMBERS!")
        return False


# Checks for the winner
def check_winner(hand):
    """
    Checks for the winner of the game
    """

    card_values = []

    duplicate_pair_1 = None
    duplicate_pair_2 = None
    duplicate_cards = []
    matching_pair = False

    unique_card_values = None
    unique_cards = []
    sequential_cards = []
    sequential_pair = False

    winning_cards = []

    """
    The player holds 4 cards at this point. we want to know if any of the cards are duplicates or
    sequential to each other...
    
    After which we will make a list of the duplicates and sequential cards to be combined later.
    """

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
                time.sleep(0.5)

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
        winner = False
        print(f"ALL CARDS ARE UNIQ CARDS = {hand} \n")
        time.sleep(0.5)
        print("Close but No cigar! You must drop a card for the next player to go!")
        # Now go to next_player()
        return winner

    if matching_pair:
        print(f"IF DUPLICATE CARDS = {duplicate_cards}")
        for card in range(len(hand)):
            if hand[card].value not in duplicate_card_values:
                unique_cards.append(hand[card])
        print(f"THEN UNIQUE CARDS = {unique_cards}")

        # Bool - Checks for consecutive numbers for the cards - Returns True or False
        sequential_pair = check_for_sequence(unique_card_values)
        if sequential_pair:
            sequential_cards = unique_cards
            print(f"THE UNIQUE CARDS = {unique_cards} ARE SEQUENTIAL!")

        else:
            winner = False
            print("Close but No cigar! You must drop a card for the next player to go!")
            return winner

    if matching_pair and sequential_pair:
        winner = True
        winning_cards.extend(duplicate_cards)
        winning_cards.extend(sequential_cards)
        print(f"WINNING CARDS = {winning_cards}")
        return winner


def players_init():
    """
    Initialize the number of players, their names and their hands.
    Numbers of players is variable. max number will be 5 players
    :return: A list of players
    """

    num_of_players = int(input("Enter the number of player: "))
    players_list = []
    for i in range(num_of_players):
        # Instantiate player objects and initialise their hands
        players_list.append(Player(input(f"Enter Player {i + 1}'s name: ")))
    return players_list, num_of_players


def first_drawer(players, number_of_players):
    random_num = random.randint(0, number_of_players)
    first_player = players[random_num - 1]
    return first_player


# LET THE GAMES BEGIN!!!

players_list, num_of_players = players_init()

restart = False
game_over = False

# Initializes a card deck, card pool, shuffles the cards and deals out 3 cards to each player
card_deck = cards.Deck()
card_deck.shuffle()

# Deal each player 3 cards
card_deck.deal(players_list)

# Initializes a pool where cards will be thrown.
card_pool = []

# The first player to draw is chosen at random
first_to_play = first_drawer(players_list, num_of_players)
player_index = players_list.index(first_to_play)

draw_counts = 0

# game_over = check_winner(players_list, first_hand, card_pool)
while not game_over:

    # Goes back to the first player in the list.
    if player_index == num_of_players:
        player_index = 0

    # The current player will draw a card from the deck
    current_player = players_list[player_index]
    current_player.draw(card_deck)

    # Now the game will check for a winner and return True or False in relation to the game over function
    """
    Here we can also allow the current player to make two choices:
    1. Check for a win
    2. Drop a card
    
    """


    game_over = check_winner(current_player.hand)
    time.sleep(0.5)

    # if the current player wins the game, we need to break out of the loop!
    if game_over:
        print(f"{current_player} WINS")
        break

    # We need to make sure each player does not get more that 4 cards!
    # So the current player need to drop a card before the next player can have a go!
    if len(current_player.hand) == 4:
        dropped_card = current_player.drop(current_player.hand)
        card_pool.append(dropped_card)

    try:
        print(f"{current_player.name} dropped {card_pool[-1]}")
    except:
        print("There are no cards in the Pool")

    finally:
        print(f"Card at the top of the pool is {card_pool[-1]} \n")

    player_index += 1
    draw_counts += 1
