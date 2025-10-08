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
    def __init__(self, rank, suit, visible=True):
        self.rank = rank
        self.suit = suit
        self.visible = visible

#how does card looks like
    def show(self):
        if not self.visible:
            return "Hidden Card"
        else:
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
        self.stored_cards.append(removed_card)

        print (f"Success removing {removed_card.show()} from hand.")

    def show_hand(self):
        return [card.show() for card in self.hand]

#It seems I can look at cards in my hand
    def look(self):
        return len(self.hand)

class Dealer:
    def __init__(self,deck):
        self.deck = deck
        self.hand = Hand()

    def deal_card(self, hand, visible=True):
        card = self.deck.draw()
        card.visible = visible
        hand.add_card(card)
        return card
