import cards

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.cards.pop())
        return self

    def show_hand(self):
        for c in self.hand:
            c.show()

    def __str__(self):
        return f'{self.name} =>> {self.hand}'


"""

print(f"{bob.name} drew the card ", end="")
bob.show_hand()

"""
