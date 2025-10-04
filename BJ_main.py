from MyPython.BJ_classes import *

# Testing the classes
deck = Deck()
my_hand = Hand()
card1 = deck.draw()
my_hand.add_card(card1)
card2 = deck.draw()
my_hand.add_card(card2)
print(my_hand.look())
print(deck.look_deck())
dealer = Dealer()
dealer.reshuffle()