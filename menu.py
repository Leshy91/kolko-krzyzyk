import sys
import gameboard
import game


class Menu:

    def __init__(self):
        print("Tworzenie menu...")


    def call_menu(self):
        print("\nWybierz co chcesz zrobić wpisując odpowiednią cyfrę: ")
        print("""
        1 - Nowa gra
        2 - Wczytaj grę
        3 - Zapisz grę
        4 - Powtórka ostatniej rozgrywki
        5 - Wyjście
        """)
        return input()

        ###if menu_choice == '1':
            ###return '1'
        ###elif menu_choice == '2':
            ###return '2'
        ###elif menu_choice == '3':
            ###return '3'
        ###elif menu_choice == '4':
            ###return '4'
        ###elif menu_choice == '5':
            ###return '5'
