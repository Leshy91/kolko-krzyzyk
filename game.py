import gameboard
import exceptions
import os


class Game:

    def __init__(self, board_min, board_max, size=None):
        print("Tworzenie nowej gry...\n")
        if size is None:
            while True:
                try:
                    self.gamesize = int(input(f"\nPodaj rozmiar planszy na której chcesz grać (nie mniej niż "
                                              f"{board_min}, nie więcej niż {board_max}): "))
                    if self.gamesize < board_min or self.gamesize > board_max:
                        raise exceptions.NotInRangeError()
                    self.gameboard = gameboard.GameBoard(self.gamesize)
                    break
                except ValueError:
                    print(f"\nNiepoprawna wartość! Rozmiar planszy musi być liczbą całkowitą z przedziału od "
                          f"{board_min} do {board_max}")
                except exceptions.NotInRangeError:
                    print(f"Rozmiar planszy musi znajdować się w przedziale od {board_min} do {board_max}")
        else:
            try:
                self.gameboard
            except AttributeError:
                self.gameboard = gameboard.GameBoard(size)

    def new_game(self):
        self.gameboard.make_board()
        print(self.gameboard)
        self.save_replay('w', self.gameboard.size)

    def load_game(self, player1, player2, saved_game):
        move1 = saved_game[4] == "True"
        move2 = saved_game[8] == "True"
        player1.create_player(saved_game[1], saved_game[2], saved_game[3], move1)
        player2.create_player(saved_game[5], saved_game[6], saved_game[7], move2)
        self.gameboard.load_board(saved_game)
        print(self.gameboard)
        if self.gameboard.if_win(player1.mark) or self.gameboard.if_win(player2.mark):
            print("\nZapisana gra jest już rozstrzygnięta\n")
            return
        self.save_replay('w', self.gameboard.size)
        while board_status := self.gameboard.if_full():
            if self.match(player1, player2):
                break

    def match(self, player1, player2):

        if not player1.if_moved:
            while not player1.if_moved:
                player_move = player1.make_move()
                if player_move == 'save':
                    print("Zapisz grę\n")
                    self.save_game(player1.name, player1.mark, player1.points, player1.if_moved, player2.name,
                                   player2.mark, player2.points, player2.if_moved)
                elif player_move == 'menu':
                    return True
                elif self.gameboard.make_mark(player_move, player1.mark):
                    print(self.gameboard)
                    player1.if_moved = True
                else:
                    print("\a")
            self.save_replay('a', self.gameboard.size)

            if self.gameboard.if_win(player1.mark):
                print(f"\nZwyciężył gracz {player1.name}\n")
                player1.points += 1
                print(f"\nIlość punktów gracza {player1.name}: {player1.points}")
                print(f"Ilość punktów gracza {player2.name}: {player2.points}\n")
                return True
            if not self.gameboard.if_full():
                print("\nRemis!\n")
                print(f"\nIlość punktów gracza {player1.name}: {player1.points}")
                print(f"Ilość punktów gracza {player2.name}: {player2.points}\n")
                return True

        if not player2.if_moved:
            while not player2.if_moved:
                player_move = player2.make_move()
                if player_move == 'save':
                    print("Zapisz grę\n")
                    self.save_game(player1.name, player1.mark, player1.points, player1.if_moved, player2.name,
                                   player2.mark, player2.points, player2.if_moved)
                elif player_move == 'menu':
                    return True
                elif self.gameboard.make_mark(player_move, player2.mark):
                    print(self.gameboard)
                    player2.if_moved = True
                else:
                    print("\a")

            self.save_replay('a', self.gameboard.size)

            if self.gameboard.if_win(player2.mark):
                print(f"\nZwyciężył gracz {player2.name}\n")
                player2.points += 1
                print(f"\nIlość punktów gracza {player2.name}: {player2.points}")
                print(f"Ilość punktów gracza {player1.name}: {player1.points}\n")
                return True

        player1.if_moved = False
        player2.if_moved = False

    def save_game(self, player1_name, player1_mark, player1_points, player1_ifmoved, player2_name, player2_mark,
                  player2_points, player2_ifmoved):
        with open('save.txt', 'w') as save:
            save.write(f"{self.gameboard.size}${player1_name}${player1_mark}${str(player1_points)}$"
                       f"{str(player1_ifmoved)}${player2_name}${player2_mark}${str(player2_points)}$"
                       f"{str(player2_ifmoved)}")
            for row in self.gameboard.board:
                for item in row:
                    save.write(f"${item}")

    def save_replay(self, file_mode, board_size):
        with open('replay.txt', file_mode) as replay:
            if file_mode == 'w':
                replay.write(str(board_size))
                replay.write('\n')
            for row in self.gameboard.board:
                for item in row:
                    replay.write(str(item))
                replay.write("\n")

    def load_replay(self):
        if os.path.isfile("replay.txt"):
            turns = []
            with open("replay.txt", 'r') as replay:

                size = int(replay.readline())
                turns_count = int((len(replay.readlines())) / size)

                replay.seek(0, 0)
                replay.readline()

                for _ in range(turns_count):
                    help_list = []
                    for _ in range(size):
                        help_list.append(replay.readline())
                    turns.append(help_list)

            index = 0
            while index < len(turns):
                for item in turns[index]:
                    print(item)
                if index == 0 and len(turns) > 1:
                    while True:
                        choice = input("\nNaciśnij 'n' by przejść do następnego ruchu, naciśnij 'q' by wyjść do menu: ")
                        if choice.lower() == 'q':
                            return
                        elif choice.lower() == 'n':
                            print(f"\nRuch numer {index + 1}")
                            index += 1
                            break
                        else:
                            print("\nNie rozumiem, spróbuj jeszcze raz...")
                elif index == len(turns) - 1 and len(turns) > 1:
                    while True:
                        choice = input("\nNaciśnij 'p' by przejść do poprzedniego ruchu, naciśnij 'q' "
                                       "by wyjść do menu:")
                        if choice.lower() == 'q':
                            return
                        elif choice.lower() == 'p':
                            print(f"\nRuch numer {index - 1}")
                            index -= 1
                            break
                        else:
                            print("\nNie rozumiem, spróbuj jeszcze raz...")
                elif index == 0 and len(turns) == 1:
                    while True:
                        choice = input("\nZapisana partia ma tylko jedną planszę, naciśnij 'q' by wyjść do menu: ")
                        if choice.lower() == 'q':
                            return
                        else:
                            print("\nNie rozumiem, spróbuj jeszcze raz...")
                else:
                    while True:
                        choice = input("\nWpisz 'n' by przejść do następnego ruchu, wpisz 'p' by przejść do "
                                       "poprzedniego ruchu, naciśnij 'q' by wyjść do menu: ")
                        if choice.lower() == 'q':
                            return
                        elif choice.lower() == 'n':
                            print(f"\nRuch numer {index + 1}")
                            index += 1
                            break
                        elif choice.lower() == 'p':
                            print(f"\nRuch numer {index - 1}")
                            index -= 1
                            break
                        else:
                            print("\nNie rozumiem, spróbuj jeszcze raz...")

        else:
            print("Brak zapisanej powtórki. Rozegraj przynajmniej jedną partię by zobaczyć powtórkę.")
