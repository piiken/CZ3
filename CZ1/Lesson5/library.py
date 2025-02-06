def show_books(books):
    """Wyświetla listę książek."""
    print("\nTwoje ksiazki:")
    for book in books:
        print(f"- {book}")  # Wypisuje każdy tytuł książki na nowej linii

def add_book(books, book):
    """Dodaje nową książkę do listy."""
    books.append(book)  # Dodaje książkę do listy
    print(f"dodano ksiązke: {book}")

def remove_book(books, book):
    """Usuwa książkę z listy, ignorując wielkość liter."""
    for original_book in books:
        if original_book.lower() == book.lower():  # Porównuje tytuły bez względu na wielkość liter
            books.remove(original_book)  # Usuwa znalezioną książkę
            print(f"Usunięto ksiązke: {original_book}")
            return  # Przerywa działanie funkcji po usunięciu książki
    print(f"książka {book} nie znajduje się na liście")

# Główna logika programu
books = ["Hobbit", "Lalka", "Gra o Tron"]  # Lista przechowująca książki

while True:
    print("\nWybierz opcję:")
    print("1. Wyświetl książki")
    print("2. Dodaj książkę")
    print("3. Usuń książkę")
    print("4. Wyjdź")

    choice = input("Wybór: ").strip()  # Pobiera wybór użytkownika i usuwa zbędne spacje
    if choice == "1":
        show_books(books)  # Wyświetla listę książek
    elif choice == "2":
        new_book = input("Podaj tytuł książki do dodania: ").strip()  # Pobiera tytuł od użytkownika
        if not new_book:
            print("Nie podałeś tytułu książki!")
        elif any(new_book.lower() == b.lower() for b in books):  # Sprawdza, czy książka już istnieje (ignorując wielkość liter)
            print("Ta książka jest już na liście!")
        else:
            add_book(books, new_book)  # Dodaje nową książkę
    elif choice == "3":
        book_to_remove = input("Podaj tytuł książki do usunięcia: ").strip()  # Pobiera tytuł książki do usunięcia
        if not book_to_remove:
            print("Nie podałeś tytułu książki!")
        else:
            remove_book(books, book_to_remove)  # Usuwa książkę, jeśli istnieje
    elif choice == "4":
        print("Good Bye!")
        break  # Kończy działanie programu
    else:
        print("Nieprawidłowy wybór!")  # Obsługuje błędne wpisy użytkownika
