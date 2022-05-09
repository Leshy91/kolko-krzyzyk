
class GameBoard:

    def __init__(self, size):
        print("\nTworzenie planszy...\n")
        self.board = []
        self.size = size

    def make_board(self):
        self.board.clear()
        for _ in range(self.size):
            help_list = [' - ' for _ in range(self.size)]
            self.board.append(help_list)
        # self.board = [' - ' for _ in range(self.size) for _ in range (self.size)]

    def __str__(self):
        print()
        print(" ", end='')
        for i in range(self.size):
            print(f" {i + 1} ", end='')
        print()
        for k, i in enumerate(self.board):
            print(k + 1, end='')
            for j in i:
                print(j, end='')
            print()
        return '\n'

    def load_board(self, saved_list):
        self.board.clear()
        ind = 9   # od tej pozycji w pliku save zaczynają się znaki na tablicy zapisanej gry
        for i in range(self.size):
            help_list = []
            for j in range(self.size):
                help_list.append(saved_list[ind])
                ind += 1
            self.board.append(help_list)

    def make_mark(self, coordinates, mark):
        try:
            if coordinates[1] < 0 or coordinates[0] < 0:
                raise IndexError()
            elif self.board[coordinates[1]][coordinates[0]] == ' - ':
                self.board[coordinates[1]][coordinates[0]] = mark
                return True
            else:
                print("\nWskazana komórka jest już zajęta! SPróbuj wybrać inne pole.")
                return False
        except IndexError:
            print(f"\nWskazane pole znajduje się poza obszarem planszy! Spróbuj jeszcze raz wpisując wartości w "
                  f"przedziale od 1 do {self.size}")
            return False

    def if_full(self):
        work_list = []
        for i in self.board:
            for j in i:
                if j == ' - ':
                    work_list.append(j)
        return len(work_list)

        # wygrana w rzędach
    def win_in_row(self, mark):
        for row in self.board:
            work_list = []
            for item in row:
                if item == mark:
                    work_list.append(item)
            if len(work_list) == self.size:
                return True

        # wygrana w kolumnach
    def win_in_col(self, mark):
        for i in range(self.size):
            work_list = []
            for row in self.board:
                if row[i] == mark:
                    work_list.append(row[i])
            if len(work_list) == self.size:
                return True

        # wygrana na krzyż
    def win_in_cross(self, mark):
        j = self.size - 1
        work_list = []
        for row in self.board:
            if row[j] == mark:
                work_list.append(row[j])
                j -= 1
            else:
                break
        if len(work_list) == self.size:
            return True

        j = 0
        work_list.clear()
        for row in self.board:
            if row[j] == mark:
                work_list.append(row[j])
                j += 1
            else:
                break
        if len(work_list) == self.size:
            return True
        else:
            return False

    def if_win(self, mark):
        return self.win_in_row(mark) or self.win_in_col(mark) or self.win_in_cross(mark)
