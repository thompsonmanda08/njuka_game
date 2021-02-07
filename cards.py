import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def display(self):
        if self.value == 1:
            print(f"{'A'} of {self.suit}")
        else:
            print(f"{self.value} of {self.suit}")

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Hearts", "Spades", "Clubs", "Diamonds"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def show(self):
        for card in self.cards:
            card.display()

    def shuffle(self):
        # assigns i a number between 0 and total number of cards -1, counting backwards from the total number of cards
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)  # Assigns a random between 0 and i to the r variable
            # swap card at position i with card at random number r
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def deal(self, players_list):
        # deals 3 cards to each player in the players_list of the game
        for player in players_list:
            player.hand = self.cards[-3:]
            self.cards = self.cards[:-3]

    def __str__(self):
        return f"{self.cards}"


