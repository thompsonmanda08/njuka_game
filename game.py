import cards
from players import Player


def game_players():
    # initialize the number of players, their names and their hands.
    # numbers of players is variable. max number will be 5 players
    number_of_players = int(input("Enter the number of player: "))
    players_list = []
    for i in range(number_of_players): # Initialising a list of players
        # Instantiate player objects and initialise their hands
        players_list.append(Player(input(f"Enter Player {i + 1}'s name: ")))
    return players_list


players = game_players()
deck = cards.Deck()
deck.shuffle()

a = list(deck.cards)
print(a)
print(len(a))

deck.deal(players)

b = list(deck.cards)
print(b)
print(len(b))


