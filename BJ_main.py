from MyPython.BJ_classes import *

# Testing the classes
deck = Deck()
card1 = deck.draw()
my_hand = Hand()
my_store = Hand()
dealer = Dealer(deck)
card2 = deck.draw()
my_hand.add_card(card1)
my_hand.add_card(card2)
card3 = deck.draw()
dealer.hand.add_card(card3)
print(card1.show())
print(card2.show())
print(card3.show())
print(my_hand.look())
print(deck.look_deck())

print(deck.look_deck())
dealer.deal_card(dealer.hand, visible=False)
dealer.hand.show_hand()
