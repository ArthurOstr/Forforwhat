import random
class Deck:
    def __init__(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["Jack", "Queen", "King", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10" ]
        self.cards = [Card(rank,suit) for rank in ranks for suit in suits]

#taking 1 card from the deck
    def draw(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

#how does card looks like
    def show(self):
        return f"{self.rank} of {self.suit}"


class Hand:
    def __init__(self):
        self.hand = []

#It seems i can look at cards in my hand
    def look(self):
        return self.card.show()

class Dealer:
    def __init__(self):
        self.deck = Deck()

if __name__ == "__main__":
    print("this is logic file")

# i need to enhance Hand methods, add more logic to dealer and add class Game to connect it with other classes