def show_books(books):
    print("\nTwoje ksiazki:")
    for book in books:
        print(f"- {book}")

def add_book(books, book):
    books.append(book)
    print(f"dodano ksiązke: {book}")

def remove_book(books, book):
    for original_book in books:
        if original_book.lower() == book.lower():
            books.remove(original_book)
            print(f"Usunięto ksiązke: {original_book}")
            return
    print(f"książka {book} nie znajduje się na liście")

# Główna logika programu
books = ["Hobbit", "Lalka", "Gra o Tron"]

while True:
    print("\nWybierz opcję:")
    print("1. Wyświetl książki")
    print("2. Dodaj książkę")
    print("3. Usuń książkę")
    print("4. Wyjdź")

    choice = input("Wybór: ").strip()
    if choice == "1":
        show_books(books)
    elif choice == "2":
        new_book = input("Podaj tytuł książki do dodania: ").strip()
        if not new_book:
            print("Nie podałeś tytułu książki!")
        elif any(new_book.lower() == b.lower() for b in books):
            print("Ta książka jest już na liście!")
        else:
            add_book(books, new_book)
    elif choice == "3":
        book_to_remove = input("Podaj tytuł książki do usunięcia: ").strip()
        if not book_to_remove:
            print("Nie podałeś tytułu książki!")
        else:
            remove_book(books, book_to_remove)
    elif choice == "4":
        print("Good Bye!")
        break
    else:
        print("Nieprawidłowy wybór!")
