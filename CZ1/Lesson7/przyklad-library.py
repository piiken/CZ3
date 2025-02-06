FILENAME = "books.txt"

# Funkcja do wczytywania książek z pliku
def load_books():
    try:
        with open(FILENAME, "r", encoding="utf-8") as plik:
            books = {}
            for line in plik:
                parts = line.strip().split(" - ")  # Rozdzielamy tytuł i autora
                if len(parts) == 2:
                    books[parts[0]] = parts[1]  # Tytuł jako klucz, autor jako wartość
            return books
    except FileNotFoundError:
        return {}  # Jeśli plik nie istnieje, zwracamy pusty słownik

# Funkcja do zapisywania książek do pliku
def save_books(books):
    with open(FILENAME, "w", encoding="utf-8") as plik:
        for title, author in books.items():
            plik.write(f"{title} - {author}\n")  # Zapisujemy tytuł i autora w jednej linii

books = load_books()  # Wczytujemy książki z pliku na starcie programu

def show_books():
    """Wyświetla listę książek."""
    if books:
        print("\nTwoje książki:")
        for title, author in books.items():
            print(f"- {title} (autor: {author})")
    else:
        print("\nBrak książek w bibliotece.")

def add_book(title, author):
    """Dodaje nową książkę do listy."""
    if title.lower() in (t.lower() for t in books):  # Sprawdzamy, czy książka już istnieje
        print(f"Książka '{title}' już jest w bibliotece!")
    else:
        books[title] = author
        save_books(books)  # Zapisujemy zmiany do pliku
        print(f"Dodano książkę: {title} (autor: {author})")

def remove_book(title):
    """Usuwa książkę z listy."""
    for original_title in books:
        if original_title.lower() == title.lower():  # Ignorujemy wielkość liter
            del books[original_title]
            save_books(books)  # Aktualizujemy plik po usunięciu
            print(f"Usunięto książkę: {original_title}")
            return
    print(f"Książka '{title}' nie znajduje się w bibliotece!")

def find_author(title):
    """Znajduje autora książki."""
    for original_title, author in books.items():
        if original_title.lower() == title.lower():
            print(f"Książkę '{original_title}' napisał {author}.")
            return
    print(f"Książka '{title}' nie znajduje się w bibliotece!")

# Główna logika programu
while True:
    print("\nWybierz opcję:")
    print("1. Wyświetl książki")
    print("2. Dodaj książkę")
    print("3. Usuń książkę")
    print("4. Znajdź autora")
    print("5. Wyjdź")

    choice = input("Wybór: ").strip()
    if choice == "1":
        show_books()
    elif choice == "2":
        title = input("Podaj tytuł książki: ").strip()
        author = input("Podaj autora książki: ").strip()
        add_book(title, author)
    elif choice == "3":
        title = input("Podaj tytuł książki do usunięcia: ").strip()
        remove_book(title)
    elif choice == "4":
        title = input("Podaj tytuł książki, której autora chcesz znaleźć: ").strip()
        find_author(title)
    elif choice == "5":
        print("Do zobaczenia!")
        break
    else:
        print("Nieprawidłowy wybór, spróbuj ponownie.")

