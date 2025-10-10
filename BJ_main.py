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
        # Check deck size
        if deck.look_deck() < 15:
            deck.restart()
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
        dealer.deal_card(visible=True)
        dealer.deal_card(visible=False)
        player.get_card()
        player.get_card()

        # player turn
        player_busted = False
        while True:
            show_table(player, dealer)
            choice = input("Hit or Stand? (h/s): ").lower()
            if choice == 'h':
                player.get_card()
                dealer.deal_card(visible=False)
                if player.hand.get_value() > 21:
                    print("Player busts!")
                    player_busted = True
                    break
            elif choice == 's':
                break

        # Dealer's turn only if player hasn't busted
        if not player_busted:
            dealer.reveal()  # Reveal dealer's hidden card
            while dealer.hand.get_value() < 17:
                dealer.deal_card()

            # value comparison
            show_table(player, dealer)
            player_value = player.hand.get_value()
            dealer_value = dealer.hand.get_value()

            if dealer_value > 21:
                print("Dealer busts! Player wins!")
                player.win_bet()
            elif player_value > dealer_value:
                print("Player wins!")
                player.win_bet()
            elif dealer_value > player_value:
                print("Dealer wins!")
                player.lose_bet()
            else:
                print("Push - it's a tie!")
                player.push_bet()
        else:
            player.lose_bet()

        if player.balance <= 0:
            print("Game over! You're out of money!")
            break

        # Ask to play again
        if not input("Play another round? (y/n): ").lower().startswith('y'):
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()