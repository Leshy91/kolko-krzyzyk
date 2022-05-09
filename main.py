import menu
import game
import player
import sys
import os

CROSS_SYMBOL = ' X '
CIRCLE_SYMBOL = ' O '
EMPTY_SYMBOL = ' - '
BOARD_MIN = 3
BOARD_MAX = 9

print("\nUruchamianie gry...")

Player1 = player.Player()
Player2 = player.Player()

choice = 'n'
if os.path.isfile("save.txt"):
    choice = input(
        "\nCzy chcesz wczytać ostatnio zapisaną grę? (wpisz 't' żeby potwierdzić lub dowolną inną wartość "
        "żeby kontynuować)")
    if choice.lower() == 't':
        with open("save.txt", 'r') as load_file:
            saved_game = load_file.readline().split('$')
            new_game = game.Game(BOARD_MIN, BOARD_MAX, int(saved_game[0]))
            new_game.load_game(Player1, Player2, saved_game)
if choice.lower() != 't':
    while True:
        mark = input("\nWybierz swój symbol 'X' lub 'O': ")
        if mark.lower() == 'x':
            name1 = input("\nPodaj swoją nazwę: ")
            Player1.create_player(name1, CROSS_SYMBOL)
            while True:
                name2 = input("\nPodaj swoją nazwę: ")
                if name2 == name1:
                    print(f"\nNazwy graczy muszą się różnić, wprowadź nazwę inną niż {Player1.name}")
                else:
                    Player2.create_player(name2, CIRCLE_SYMBOL)
                    break
            break
        elif mark.lower() == 'o':
            name1 = input("Podaj swoją nazwę: ")
            Player1.create_player(name1, CIRCLE_SYMBOL)
            while True:
                name2 = input("Podaj swoją nazwę: ")
                if name2 == name1:
                    print(f"\nNazwy graczy muszą się różnić, wprowadź nazwę inną niż {Player1.name}")
                else:
                    Player2.create_player(name2, CROSS_SYMBOL)
                    break
            break
        else:
            print("Nie wybrano poprawnego symbolu, spróbuj jeszcze raz.")

new_menu = menu.Menu()

try:
    new_game
except NameError:
    new_game = game.Game(BOARD_MIN, BOARD_MAX)

while True:
    menu_choice = new_menu.call_menu()

    if menu_choice == '1':
        print("\nNOWA GRA\n")
        new_game.new_game()

        while board_status := new_game.gameboard.if_full():
            if new_game.match(Player1, Player2):
                break

    elif menu_choice == '2':
        print("\nZAPISZ GRĘ\n")
        new_game.save_game(Player1.name, Player1.mark, Player1.points, Player1.if_moved, Player2.name, Player2.mark,
                           Player2.points, Player2.if_moved)

    elif menu_choice == '3':
        print("\nPOWTÓRKA\n")
        new_game.load_replay()

    elif menu_choice == '4':
        print("\nTABLICA WYNIKÓW\n\n")
        print(f"\nIlość punktów gracza {Player1.name}: {Player1.points}")
        print(f"Ilość punktów gracza {Player2.name}: {Player2.points}\n")

    elif menu_choice == '5':
        print("\nWYJŚCIE\n")
        sys.exit()

    else:
        print("Nie wybrano żadnej z opcji...")
