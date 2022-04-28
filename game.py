import gameboard
import menu
import datetime

class Game:

    def __init__(self):
        print("Tworzenie nowej gry...\n")
        self.gameboard = gameboard.game_board()


    def new_game(self):
        self.gameboard.make_board()
        self.gameboard.draw_board()


    def load_game(self, Player1, Player2):
        self.gameboard.draw_board()
        load_file = open("save.txt", 'r')
        saved_game = load_file.readline().split('$')
        Player1.name = saved_game[1]
        Player1.mark = saved_game[2]
        Player1.points = int(saved_game[3])
        #Player1.if_moved = True if saved_game[4] == "True" else Player1.if_moved = False
        if saved_game[4] == "True":
            Player1.if_moved = True
        else:
            Player1.if_moved = False
        Player2.name = saved_game[5]
        Player2.mark = saved_game[6]
        Player2.points = int(saved_game[7])
        #Player2.if_moved = True if saved_game[8] == "True" else Player2.if_moved = False
        if saved_game[8] == "True":
            Player2.if_moved = True
        else:
            Player2.if_moved = False
        self.gameboard.load_board(saved_game)
        self.gameboard.draw_board()
        board_status = self.gameboard.if_full()
        while board_status:
            if self.match(Player1, Player2):
                break
            board_status = self.gameboard.if_full()


    def match(self, Player1, Player2):

        if Player1.if_moved == False:
            while Player1.if_moved == False:
                self.player_move = Player1.make_move()
                if self.player_move == 'save':
                    print("Zapisz grę\n")
                    self.save_game(Player1.name, Player1.mark, Player1.points, Player1.if_moved, Player2.name, Player2.mark, Player2.points, Player2.if_moved)
                elif self.gameboard.make_mark(self.player_move[0], self.player_move[1], Player1.mark):
                    self.gameboard.make_mark(self.player_move[0], self.player_move[1], Player1.mark)
                    self.gameboard.draw_board()
                    Player1.if_moved = True
                else:
                    print('\a')
                    print("\nKomórka jest już zajęta lub podałeś indeks spoza planszy, spróbuj postawić znak w innym miejscu\n")

            if self.gameboard.if_win(Player1.mark):
                print(f"\nZwyciężył gracz {Player1.name}\n")
                Player1.points += 1
                print(f"\nIlość punktów gracza {Player1.name}: {Player1.points}")
                print(f"Ilość punktów gracza {Player2.name}: {Player2.points}\n")
                return True
            if not self.gameboard.if_full():
                print("\nRemis!\n")
                print(f"\nIlość punktów gracza {Player1.name}: {Player1.points}")
                print(f"Ilość punktów gracza {Player2.name}: {Player2.points}\n")
                return True

        if Player2.if_moved == False:
            while Player2.if_moved == False:
                self.player_move = Player2.make_move()
                if self.player_move == 'save':
                    print("Zapisz grę\n")
                    self.save_game(Player1.name, Player1.mark, Player1.points, Player1.if_moved, Player2.name, Player2.mark, Player2.points, Player2.if_moved)
                elif self.gameboard.make_mark(self.player_move[0], self.player_move[1], Player2.mark):
                    self.gameboard.make_mark(self.player_move[0], self.player_move[1], Player2.mark)
                    self.gameboard.draw_board()
                    Player2.if_moved = True
                else:
                    print('\a')
                    print("\nKomórka jest już zajęta lub podałeś indeks spoza planszy, spróbuj postawić znak w innym miejscu\n")

            if self.gameboard.if_win(Player2.mark):
                print(f"\nZwyciężył gracz {Player2.name}\n")
                Player2.points += 1
                print(f"\nIlość punktów gracza {Player2.name}: {Player2.points}")
                print(f"Ilość punktów gracza {Player1.name}: {Player1.points}\n")
                return True

        Player1.if_moved = False
        Player2.if_moved = False


    def save_game(self, player1_name, player1_mark, player1_points, player1_ifmoved, player2_name, player2_mark, player2_points, player2_ifmoved):
        self.player1_name = player1_name
        self.player1_mark = player1_mark
        self.player1_points = str(player1_points)
        self.player1_ifmoved = player1_ifmoved
        self.player2_name = player2_name
        self.player2_mark = player2_mark
        self.player2_points = str(player2_points)
        self.player2_ifmoved = player2_ifmoved
        #self.board = board
        date = str(datetime.datetime.now())
        save = open('save.txt', 'w')
        save.write(date + '$' + player1_name + '$' + player1_mark + '$' + str(player1_points) + '$' + str(player1_ifmoved) + '$' + player2_name + '$' + player2_mark + '$' + str(player2_points) + '$' + str(player2_ifmoved))
        for row in self.gameboard.board:
            for item in row:
                save.write('$' + item)
        save.close()
