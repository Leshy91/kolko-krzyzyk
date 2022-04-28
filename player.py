import sys

class Player:

    def __init__(self, mark):
        self.name = input(f"Tworzenie gracza z symbolem {mark}, podaj swoje imię: ")
        self.points = 0
        self.mark = ' ' + mark + ' '
        print(f"\nUtworzono nowego gracza: {self.name}\n")


    def make_move(self):
        print(f"\n{self.name} w którym miejscu chcesz umieścić swój znak?\n(jeśli chcesz zakończyć grę wpisz 'q' lub 'Q')\n(jeśli chcesz zapisać grę wpisz 's' lub 'S')\n")
        self.col = input("Podaj numer kolumny: ")
        if self.col == 'q' or self.col == 'Q':
            sys.exit()
        elif self.col == 's' or self.col == 'S':
            return 'save'
        else:
            try:
                self.col = int(self.col)
                self.row = int(input("Podaj numer wiersza: "))
                self.coordinates = [self.col, self.row]
                return self.coordinates
            except ValueError:
                print("Niewłaściwa wartość! Spróbuj jeszcze raz")
                return self.make_move()
