import os
from BJ_classes import Dealer, Player, Deck
import database

def login_player():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to BJ Game!")
    username = input("Please enter your username: ").strip()
    current_balance, wins = database.get_player_data(username)
    if current_balance is not None:
        return username, current_balance, wins
    else:
        print(f"User '{username}' does not exist! Create a new one!")
        new_id = database.add_player(username)

        if new_id:
            print(f"Here's a new player: {username}! His balance is ${current_balance}!")
            return username, 1000, 0
        else:
            print("Cannot create a new player!")
            return None, 0, 0
def show_table(player, dealer, reveal=False):
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n" + "=" * 20 + " ♠️♥️ BLACKJACK ♦️♣️ " + "=" * 20)
    if reveal:
        print(f"\nDealer's Hand: {dealer.hand.show_hand()}) (Value: {dealer.hand.get_value()})")
    else:
        print(f"\nDealer's Hand: {dealer.hand.show_hand()}")
    print(f"Player's Hand: {player.hand.show_hand()} (Value: {player.hand.get_value()})")
    print(f"💰 Balance: ${player.balance} | 🏆 Wins: {player.win_count}")
    print("\n" + "=" * 62 + "\n")

def play_game(username,start_balance, start_wins):
    # Initialize game components
    deck = Deck()
    dealer = Dealer(deck)
    player = Player(balance=start_balance, win_count=start_wins)

    while player.balance > 0:
        # Check deck size

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
        dealer.deal_card()
        dealer.deal_card(visible=False)
        player.receive_card(deck.draw())
        player.receive_card(deck.draw())

        # player turn
        player_busted = False
        while True:
            show_table(player, dealer, reveal=False)
            choice = input("Hit or Stand? (h/s): ").lower()
            if choice == 'h':
                player.receive_card(deck.draw())
                if player.hand.get_value() > 21:
                    print("Player busts!")
                    player_busted = True
                    break
            elif choice == 's':
                break

        # Dealer's turn
        if not player_busted:
            dealer.reveal()# Reveal dealer's hidden card
            while dealer.hand.get_value() < 17:
                dealer.deal_card()

            # value comparison
            show_table(player, dealer,reveal=True)
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
            show_table(player, dealer, reveal=True)
            print("Dealer wins!")
            dealer.reveal()
            player.lose_bet()

        if player.balance <= 0:
            print("Game over! You're out of money!")
            database.update_balance(username,0)
            break
        print(f"Saving your balance: ${player.balance}, Wins: {player.win_count}")
        database.update_balance(username,player.balance)
        database.update_win_count(username,player.win_count)

        # Ask to play again
        if not input("Play another round? (y/n): ").lower().startswith('y'):
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    database.create_tables()
    username, player_balance, player_wins = login_player()
    if username:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Welcome back, {username}! You have ${player_balance} and {player_wins} wins!")
    play_game(username,player_balance,player_wins)

    #T0 DO: count wins not only raw balance
    