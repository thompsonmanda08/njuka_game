import cards


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for c in self.hand:
            c.show()


def game_players():
    # initialize the number of players, their names and their hands.
    # numbers of players is variable. max number will be 5 players
    number_of_players = int(input("Enter the number of player: "))
    players_list = []

    for i in range(number_of_players):
        print(i)
        # players_list.append()


game_players()

"""
deck = cards.Deck()
deck.shuffle_deck()

bob = Player("Bob")
bob.draw(deck)

print(f"{bob.name} drew the card ", end="")
bob.show_hand()"""
