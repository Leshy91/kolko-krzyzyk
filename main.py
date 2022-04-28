import gameboard
import menu
import game
import player
import datetime
import sys


print("\nUruchamianie gry...")

Player1 = player.Player(mark='X')
Player2 = player.Player(mark='O')
new_menu = menu.Menu()
new_game = game.Game()

while True:
    menu_choice = new_menu.call_menu()

    if menu_choice == '1':
        print("Nowa gra\n")
        new_game.new_game()

        board_status = new_game.gameboard.if_full()
        while board_status:
            if new_game.match(Player1, Player2):
                break
            board_status = new_game.gameboard.if_full()


    elif menu_choice == '2':
        print("Wczytaj grę\n")
        print("Wersja demo. Aby korzystać z wszystkich opcji wykup pełną wersję programu\n")

    elif menu_choice == '3':
        print("Zapisz grę\n")
        new_game.save_game(Player1.name, Player1.mark, Player1.points, Player2.name, Player2.mark, Player2.points)

    elif menu_choice == '4':
        print("Powtórka\n")
        print("Wersja demo. Aby korzystać z wszystkich opcji wykup pełną wersję programu\n")

    elif menu_choice == '5':
        print("Wyjście\n")
        sys.exit()

    else:
        print("Nie wybrano żadnej z opcji...")
