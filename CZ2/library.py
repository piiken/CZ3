import json  # Moduł do obsługi JSON

BOOKS_FILE = "books.json"  # Plik do przechowywania książek

def load_books():
    """Wczytuje książki z pliku JSON"""
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)  # Wczytanie listy książek
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Jeśli plik nie istnieje lub jest pusty, zwracamy pustą listę

def save_books(books):
    """Zapisuje listę książek do pliku JSON"""
    with open(BOOKS_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4, ensure_ascii=False)  # Zapis z ładnym formatowaniem

def add_book(title, author):
    """Dodaje książkę do pliku JSON"""   
    if not title.strip() or not author.strip():
        return "❌ Tytuł i autor nie mogą być puste!"
    
    books = load_books()  # Wczytujemy aktualne książki
    books.append({"title": title, "author": author})  # Dodajemy nową książkę
    save_books(books)  # Zapisujemy do pliku
    return f"Książka '{title}' autorstwa {author} została dodana."

def list_books():
    """Zwraca listę książek z JSON"""
    books = load_books()
    if not books:
        return "Brak książek w bibliotece."
    
    return "\n".join([f"- {book['title']} ({book['author']})" for book in books])

def remove_book(title):
    """Usuwa książkę z listy na podstawie tytułu"""
    if not title.strip():
        return "❌ Tytuł książki nie może być pusty!"
    
    books = load_books()
    new_books = [book for book in books if book["title"].lower() != title.lower()]

    if len(new_books) == len(books):  # Jeśli nie zmieniła się długość listy, książki nie znaleziono
        return f"Nie znaleziono książki '{title}'."

    save_books(new_books)  # Zapisujemy nową listę książek
    return f"Książka '{title}' została usunięta."

def edit_book(title, new_author):
    """Edytuje autora książki na podstawie tytułu"""
    if not title.strip() or not new_author.strip():
        return "❌ Tytuł i nowy autor nie mogą być puste!"
   
    books = load_books()
    for book in books:
        if book["title"].lower() == title.lower():
            book["author"] = new_author
            save_books(books)
            return f"Zmieniono autora książki '{title}' na {new_author}."

    return f"Nie znaleziono książki '{title}'."

def find_book(title):
    """Wyszukuje książkę po tytule"""
    books = load_books()
    for book in books:
        if title.lower() in book["title"].lower():
            return f"🔍 Znaleziono: {book['title']} ({book['author']})"

    return f"❌ Nie znaleziono książki '{title}'."

