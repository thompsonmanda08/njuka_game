class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value= value

    def show(self):
        if self.value == 1:
            print(f"{'A'} of {self.suit}")
        else:
            print(f"{self.value} of {self.suit}")


class Deck():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Hearts", "Spades", "Clubs", "Diamonds"]:
            for value in range(1,11):
                self.cards.append(Card(suit, value))

    def show(self):
        for card in self.cards:
            card.show()



card = Card("H", 7)
card.show()

print("\n\n")

deck = Deck()
deck.show()