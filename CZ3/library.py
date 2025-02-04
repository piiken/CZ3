import sqlite3
import csv
import random
import os

DB_FILE = "books.db"

# 📌 Tworzenie bazy danych, jeśli nie istnieje
def init_db():
    """Tworzy bazę danych, jeśli nie istnieje"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# 📌 Dodawanie książki do bazy
def add_book(title, author):
    """Dodaje książkę do bazy danych"""
    if not title.strip() or not author.strip():
        return "❌ Tytuł i autor nie mogą być puste!"

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    conn.close()
    return f"✅ Książka '{title}' autorstwa {author} została dodana."

# 📌 Wyświetlanie listy książek
def list_books():
    """Zwraca listę książek"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT title, author FROM books")
    books = cursor.fetchall()
    conn.close()

    if not books:
        return "📭 Brak książek w bibliotece."

    return "\n".join([f"- {book[0]} ({book[1]})" for book in books])

# 📌 Usuwanie książki
def remove_book(title):
    """Usuwa książkę z bazy danych"""
    if not title.strip():
        return "❌ Tytuł książki nie może być pusty!"

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE title = ?", (title,))
    conn.commit()
    deleted_rows = cursor.rowcount
    conn.close()

    if deleted_rows == 0:
        return f"❌ Nie znaleziono książki '{title}'."
    return f"✅ Książka '{title}' została usunięta."

# 📌 Edytowanie autora książki
def edit_book(title, new_author):
    """Edytuje autora książki na podstawie tytułu"""
    if not title.strip() or not new_author.strip():
        return "❌ Tytuł i nowy autor nie mogą być puste!"

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET author = ? WHERE title = ?", (new_author, title))
    conn.commit()
    updated_rows = cursor.rowcount
    conn.close()

    if updated_rows == 0:
        return f"❌ Nie znaleziono książki '{title}'."
    return f"✅ Zmieniono autora książki '{title}' na {new_author}."

# 📌 Wyszukiwanie książki po tytule
def find_book(title):
    """Wyszukuje książkę po tytule"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT title, author FROM books WHERE title LIKE ?", ('%' + title + '%',))
    books = cursor.fetchall()
    conn.close()

    if not books:
        return f"❌ Nie znaleziono książki '{title}'."
    
    return "\n".join([f"🔍 {book[0]} - {book[1]}" for book in books])

# 📌 Eksportowanie książek do pliku .txt lub .csv
def export_books(format="txt"):
    """Eksportuje książki do pliku .txt lub .csv"""
    books = list_books().split("\n")

    if not books or books[0] == "📭 Brak książek w bibliotece.":
        return "❌ Brak książek do eksportu."

    if format == "txt":
        with open("books.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(books))
        return "✅ Książki zapisane do books.txt"

    elif format == "csv":
        with open("books.csv", "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Tytuł", "Autor"])
            for book in books:
                if " - " in book:
                    writer.writerow(book.split(" - "))
        return "✅ Książki zapisane do books.csv"

    return "❌ Nieznany format. Wybierz 'txt' lub 'csv'."

# 📌 Losowanie książki do przeczytania
def random_book():
    """Losuje książkę do przeczytania"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT title, author FROM books")
    books = cursor.fetchall()
    conn.close()

    if not books:
        return "❌ Brak książek w bibliotece."

    book = random.choice(books)
    return f"🎲 Wylosowana książka: {book[0]} - {book[1]}"
