
class Player:

    def __init__(self):
        self.name = None
        self.points = 0
        self.mark = None
        self.if_moved = False

    def create_player(self, name, mark, points=0, move=False):
        self.name = name
        self.mark = mark
        self.points = int(points)
        self.if_moved = move
        print(f"\nUtworzono nowego gracza: {self.name} ze znakiem {self.mark}, liczba punktów {self.points}")

    def make_move(self):
        choice = input(f"{self.name}, podaj numer kolumny i wiersza odzielając je spacją:"
                       f"\n(jeśli chcesz zakończyć grę wpisz 'q', jeśli chcesz zapisać grę wpisz 's')")
        if choice.lower() == 'q':
            return 'menu'
        elif choice.lower() == 's':
            return 'save'
        else:
            try:
                col, row = list(map(int, choice.split()))
                coordinates = [col - 1, row - 1]
                return coordinates
            except ValueError:
                print('\a')
                print("\nNiewłaściwa wartość! Numer kolumny i wiersza powinny być liczbami całkowitymi, "
                      "spróbuj jeszcze raz\n")
                return self.make_move()

        # if self.col == 'q' or self.col == 'Q':
        #     sys.exit()
        # elif self.col == 's' or self.col == 'S':
        #     return 'save'
        # else:
        #     try:
        #         self.col = int(self.col)
        #         self.row = int(input("Podaj numer wiersza: "))
        #         self.coordinates = [self.col, self.row]
        #         return self.coordinates
        #     except ValueError:
        #         print('\a')
        #         print("Niewłaściwa wartość! Spróbuj jeszcze raz")
        #         return self.make_move()
