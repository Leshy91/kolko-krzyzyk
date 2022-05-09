

class Menu:

    def __init__(self):
        print("Tworzenie menu...")

    def call_menu(self):
        print("\nWybierz co chcesz zrobić wpisując odpowiednią cyfrę: ")
        print("""
        1 - Nowa gra
        2 - Zapisz grę
        3 - Powtórka ostatniej rozgrywki
        4 - Wyświetl graczy i liczbę punktów
        5 - Wyjście
        """)
        return input()
