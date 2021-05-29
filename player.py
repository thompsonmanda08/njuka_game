import cards


# Defines player objects attributes and methods
class NjukaPlayer:
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
        done = False
        while not done:
            self.show_hand()
            try:
                index = int(input("\nEnter the card value you want to drop! "))
                card_index = index - 1
                drop = self.hand.pop(card_index)
                done = True
                return drop

            except:
                drop_error = "You only have 4 cards in your hand, choose numbers from 1 to 4 to pick a card!"
                return drop_error

    def show_hand(self):
        index = 1
        for card in self.hand:
            print(f"{index}.) ", end="")
            index += 1
            # print(card)
            card.display()

    def __str__(self):
        return f'{self.name} =>> {self.hand}'
