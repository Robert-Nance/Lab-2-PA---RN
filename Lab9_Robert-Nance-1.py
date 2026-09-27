
from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    play = input("Do you want to play Coin Flip? (y/n): ").strip().lower()

    while play == "y":
        player1.toss_coin()
        player2.toss_coin()

        player1side = player1.get_coin()
        player2side = player2.get_coin()

        print(f"{player1.get_name()} tossed {player1side}")
        print(f"{player2.get_name()} tossed {player2side}")

        if player1side == player2side:
            player1.win()
            player2.lose()

            print(f"{player1.get_name()} won the toss")

        else:
            player1.lose()
            player2.win()

            print(f"{player2.get_name()} won the toss")

        print(f"{player1.get_name()} has {player1.get_wallet()} coins")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins")

        play = input("Do you want to play again? (y/n): ").strip().lower()

    print("\nFinal Results:")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins")

    if player1.get_wallet() > player2.get_wallet():
        print(f"{player1.get_name()} wins")
    elif player2.get_wallet() > player1.get_wallet():
        print(f"{player2.get_name()} wins")
    else:
        print("It's a tie")

if __name__ == "__main__":
    main()