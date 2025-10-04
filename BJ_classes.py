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

#It seems i can look at cards in my deck
    def look_deck(self):
        return len(self.cards)

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

#adding card to my hand
    def add_card(self, card):
        self.hand.append(card)

#It seems i can look at cards in my hand
    def look(self):
        return len(self.hand)

class Dealer:
    def __init__(self):
        self.deck = Deck()

#reshuffle the deck when needed
    def reshuffle(self):
        self.deck = Deck()
        print(f"{self.deck.look_deck()} cards is here")



# I have two separate to run values of cards and i'm going to test them both