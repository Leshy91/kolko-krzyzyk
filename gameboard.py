
class game_board:

    def __init__(self):
        print("\nTworzenie planszy...\n")
        self.board = []


    def make_board(self):
        self.board.clear()
        for i in range(3):
            help_list = []
            for j in range(3):
                help_list.append(' - ')
            self.board.append(help_list)


    def draw_board(self):
        print()
        print(" ", end='')
        for i in range(3):
            print(f" {i} ", end='')
        print()
        k = 0
        for i in self.board:
            print(k, end='')
            for j in i:
                print(j, end='')
            k += 1
            print()
        print()


    def load_board(self, saved_list):
        self.board.clear()
        ind = 9
        for i in range(3):
            help_list = []
            for j in range(3):
                help_list.append(saved_list[ind])
                ind += 1
            self.board.append(help_list)


    def make_mark(self, col, row, mark):
        self.col = col
        self.row = row
        try:
            if self.board[row][col] == ' - ':
                self.board[row][col] = mark
                return True
            else:
                return False
        except IndexError:
                return False


    def if_full(self):
        self.work_list = []
        for i in self.board:
            for j in i:
                if j == ' - ':
                    self.work_list.append(j)
                else:
                    pass
        return len(self.work_list)


    def if_win(self, mark):
        # wygrana w rzędach
        for row in self.board:
            self.work_list = []
            for item in row:
                if item == mark:
                    self.work_list.append(item)
                else:
                    pass
            if len(self.work_list) == 3:
                return True
            else:
                pass
        # wygrana w kolumnach
        for i in range(3):
            self.work_list = []
            for row in self.board:
                if row[i] == mark:
                    self.work_list.append(row[i])
                else:
                    pass
            if len(self.work_list) == 3:
                return True
            else:
                pass
        # wygrana na krzyż
        self.j = 2
        self.work_list = []
        for row in self.board:
            if row[self.j] == mark:
                self.work_list.append(row[self.j])
                self.j -= 1
            else:
                break
        if len(self.work_list) == 3:
            return True

        self.j = 0
        self.work_list.clear()
        for row in self.board:
            if row[self.j] == mark:
                self.work_list.append(row[self.j])
                self.j += 1
            else:
                break
        if len(self.work_list) == 3:
            return True
        else:
            return False
