import cards
import random
import collections
import time
import player as P


def get_duplicates(player_hand: list[int]):
    separated_hand = None
    for potential_duplicate in player_hand:
        # here remainder is just the player's hand minus the current card we're iterating over
        remainder = player_hand.copy()
        remainder.remove(potential_duplicate)  # remainder = 3 cards

        # if the removed value is still present in remainder then we have a duplicate
        if potential_duplicate in remainder:
            remainder.remove(potential_duplicate)  # remove it again to remain with your two unique cards
            separated_hand = {
                "duplicates": [potential_duplicate, potential_duplicate],
                "unique": remainder
            }
            # break  # we break out of the loop as soon as we find the first value with a duplicate
            return separated_hand  # alternatively we could return separated_hand right inside the if block,
            # that would also break the loop
    return separated_hand


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


def collect_twin_cards(hand, dup_card_val):
    twin_cards = []
    for card in range(len(hand)):
        if hand[card].value == dup_card_val:
            twin_cards.append(hand[card])

        if len(twin_cards) == 2:
            break
    return twin_cards


# A state of having to a double duplicate card situation:
# A player must choose which card pair they would like to continue the game with!
def collision_cards(hand, dup_card_values):
    """ (list, list) -> list, list
    Returns 2 lists of card values that are identical and cause a collision
    on winning duplicate cards.

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

    dup_card_pair_1 = []
    dup_card_pair_2 = []

    assert len(dup_card_values) == 2

    for value in range(len(dup_card_values) - 1):
        dup_pair_val_1 = dup_card_values[value]
        dup_pair_val_2 = dup_card_values[value + 1]

    for card in len(hand):

        if hand[card].value == dup_pair_val_1:
            dup_card_pair_1.append(hand[card].value)

        else:
            dup_pair_val_2.append(hand[card].value)

    return dup_card_pair_1, dup_card_pair_2


def handle_collision_pairs(pair_1, pair_2):
    choice = False
    print(f"1. {pair_1}")
    print(f"2. {pair_2} \n")

    while not choice:
        try:
            choice = int(input("Choose the pair you wish to discard: "))
            if choice == 1:
                choice = True
                return pair_1

            elif choice == 2:
                choice = True
                return pair_2

        except:
            print("Enter a Number with respect to the pair you want to discard!")


# Checks for the winner
def check_winner(hand):
    """
    Checks for the winner of the game
    """

    card_values = []

    duplicate_pair_1 = None
    duplicate_pair_2 = None
    duplicate_cards = {}
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

    # check the list of card values for duplicates and returns a dictionary if any duplicates
    duplicate_cards = get_duplicates(card_values)

    if duplicate_cards is not None:
        duplicate_pair_1 = duplicate_cards['duplicates']

        # If there is more than one pair of duplicate cards the the player has a collision
        # If collision, drop 1 duplicate pair else collect duplicates & run unique cards
        if duplicate_cards['unique'][0] == duplicate_cards['unique'][1]:
            duplicate_pair_2 = duplicate_cards['unique']
            collision_cards(card_values)
        else:
            unique_cards = duplicate_cards['unique']
















def players_init():
    """
    Initialize the number of players, their names and their hands.
    Numbers of players is variable. max number will be 5 players
    :return: A list of players
    """

    num_of_players = int(input("Enter the number of player: "))
    players_list = []
    for i in range(num_of_players):
        # Instantiate player objects and initialise their hands from imported player module
        player = P.NjukaPlayer(input(f"Enter Player {i + 1}'s name: "))
        players_list.append(player)
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
