import random
class Deck:
    def __init__(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["Jack", "Queen", "King", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10" ]
        self.cards = [Card(rank,suit) for rank in ranks for suit in suits]

    def draw(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def show(self):
        return f"{self.rank} of {self.suit}"


class Hand:
    def __init__(self):
        hand = []

    def look(self):
        return self.card.show()