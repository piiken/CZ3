import os
import library
from colorama import Fore, Style, init

init(autoreset=True)

# 📌 Czyści ekran terminala
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    library.init_db()  # Inicjalizacja bazy danych

    while True:
        clear_screen()
        print(Fore.YELLOW + "📚 MENU BIBLIOTEKI 📚")
        print(Fore.GREEN + "1. Dodaj książkę")
        print(Fore.CYAN + "2. Wyświetl książki")
        print(Fore.RED + "3. Usuń książkę")
        print(Fore.BLUE + "4. Edytuj autora książki")
        print(Fore.MAGENTA + "5. Wyszukaj książkę")
        print(Fore.YELLOW + "6. Eksportuj książki (txt/csv)")
        print(Fore.GREEN + "7. Wylosuj książkę")
        print(Fore.WHITE + "8. Wyjście")

        choice = input(Fore.YELLOW + "\nWybierz opcję: ")

        if choice == "1":
            title = input(Fore.GREEN + "Podaj tytuł książki: ")
            author = input(Fore.GREEN + "Podaj autora książki: ")
            print(library.add_book(title, author))

        elif choice == "2":
            print(Fore.CYAN + "\n📖 Lista książek:")
            print(library.list_books())

        elif choice == "3":
            title = input(Fore.RED + "Podaj tytuł książki do usunięcia: ")
            print(library.remove_book(title))

        elif choice == "4":
            title = input(Fore.BLUE + "Podaj tytuł książki do edycji: ")
            new_author = input(Fore.BLUE + "Podaj nowego autora: ")
            print(library.edit_book(title, new_author))

        elif choice == "5":
            title = input(Fore.MAGENTA + "Podaj tytuł książki do wyszukania: ")
            print(library.find_book(title))

        elif choice == "6":
            format = input("Wybierz format (txt/csv): ").strip().lower()
            print(library.export_books(format))

        elif choice == "7":
            print(library.random_book())

        elif choice == "8":
            print(Fore.WHITE + "📕 Zamykanie biblioteki... Do zobaczenia!")
            break

        else:
            print(Fore.RED + "❌ Nieprawidłowy wybór! Spróbuj ponownie.")

        input(Fore.YELLOW + "\nNaciśnij ENTER, aby kontynuować...")

if __name__ == "__main__":
    main()
