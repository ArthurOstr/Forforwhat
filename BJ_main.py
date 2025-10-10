from MyPython.BJ_classes import *


def show_table(player, dealer):
    print("\n=== Current Table ===")
    print("Dealer:", dealer.hand.show_hand())
    print("Player:", player.hand.show_hand(), f"(Value: {player.hand.get_value()})")
    print("Player Balance:", player.balance)


def play_game():
    # Initialize game components
    deck = Deck()
    dealer = Dealer(deck)
    player = Player(deck, 100)

    while player.balance > 0:
        # Reset hands for new round
        dealer.hand.restart_hand()
        player.hand.restart_hand()

        # Place bet
        while True:
            try:
                bet = int(input(f"Place your bet (balance: {player.balance}): "))
                if 0 < bet <= player.balance:
                    player.place_bet(bet)
                    break
                print("Invalid bet amount")
            except ValueError:
                print("Please enter a valid number")

        # Initial deal
        dealer.deal_card(dealer.hand, visible=True)
        dealer.deal_card(dealer.hand, visible=False)
        player.get_card(player.hand)
        player.get_card(player.hand)

        # player turn
        player_turn = True
        while player_turn:
            show_table(player, dealer)
            choice = input("Hit or Stand? (h/s): ").lower()
            choice_is_hit = choice == 'h'

            if choice_is_hit:
                player.get_card(player.hand)
                if player.hand.get_value() > 21:
                    print("Player busts!")
                    player_turn = False
            else:
                player_turn = False

        # dealer turn
        while dealer.hand.get_value() < 17:
            dealer.deal_card(dealer.hand, visible=False)

        # value comparison
        show_table(player, dealer)
        player_value = player.hand.get_value()
        dealer_value = dealer.hand.get_value()

        if player_value > 21:
            print("Player busts! Dealer wins!")
            player.lose_bet()
        elif dealer_value > 21:
            print("Dealer busts! Player wins!")
            player.win_bet()
        else:
            if player_value > dealer_value:
                print("Player wins!")
                player.win_bet()
            elif dealer_value > player_value:
                print("Dealer wins!")
                player.lose_bet()
            else:
                print("Push - it's a tie!")
                player.push_bet()

        if player.balance <= 0:
            print("Game over! You're out of money!")
            break

        # Ask to play again
        if not input("Play another round? (y/n): ").lower().startswith('y'):
            break


if __name__ == "__main__":
    play_game()

