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


    def match(self, Player1, Player2):
        self.player1_moved = False
        self.player2_moved = False

        while self.player1_moved == False:
            self.player_move = Player1.make_move()
            if self.player_move == 'save':
                print("Zapisz grę\n")
                self.save_game(Player1.name, Player1.mark, Player1.points, Player2.name, Player2.mark, Player2.points)
            elif self.gameboard.make_mark(self.player_move[0], self.player_move[1], Player1.mark):
                self.gameboard.make_mark(self.player_move[0], self.player_move[1], Player1.mark)
                self.gameboard.draw_board()
                self.player1_moved = True
            else:
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

        while self.player2_moved == False:
            self.player_move = Player2.make_move()
            if self.player_move == 'save':
                print("Zapisz grę\n")
                self.save_game(Player1.name, Player1.mark, Player1.points, Player2.name, Player2.mark, Player2.points)
            elif self.gameboard.make_mark(self.player_move[0], self.player_move[1], Player2.mark):
                self.gameboard.make_mark(self.player_move[0], self.player_move[1], Player2.mark)
                self.gameboard.draw_board()
                self.player2_moved = True
            else:
                print("\nKomórka jest już zajęta lub podałeś indeks spoza planszy, spróbuj postawić znak w innym miejscu\n")

        if self.gameboard.if_win(Player2.mark):
            print(f"\nZwyciężył gracz {Player2.name}\n")
            Player2.points += 1
            print(f"\nIlość punktów gracza {Player2.name}: {Player2.points}")
            print(f"Ilość punktów gracza {Player1.name}: {Player1.points}\n")
            return True



    def save_game(self, player1_name, player1_mark, player1_points, player2_name, player2_mark, player2_points):
        self.player1_name = player1_name
        self.player1_mark = player1_mark
        self.player1_points = str(player1_points)
        self.player2_name = player2_name
        self.player2_mark = player2_mark
        self.player2_points = str(player2_points)
        #self.board = board
        date = str(datetime.datetime.now())
        save = open('save.txt', 'w')
        save.write(date + '$' + player1_name + '$' + player1_mark + '$' + str(player1_points) + '$' + player2_name + '$' + player2_mark + '$' + str(player2_points))
        for row in self.gameboard.board:
            for item in row:
                save.write('$' + item)
        save.close()
