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

#It seems I can look at cards in my deck
    def look_deck(self):
        return len(self.cards)

#reshuffle the deck when needed
    def restart(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["Jack", "Queen", "King", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        print("Deck is ready")


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
        self.stored_cards = []

#adding card to my hand
    def add_card(self, card):
        self.hand.append(card)

    def restart_hand(self):
        self.hand = []
        print("Hand is empty")

    def remove_card(self):
        if not self.hand:
            print("Hand is empty, cannot remove card.")
            return

        removed_card = self.hand.pop(0)
        removed_card.append(self.stored_cards)

        print (f"Removed card: {self.removed_card.show()}")
        #it's not done yet

#It seems I can look at cards in my hand
    def look(self):
        return len(self.hand)

class Dealer:
    def __init__(self):
        self.deck = Deck()

#reshuffle the deck when needed



