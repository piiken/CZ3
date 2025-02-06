try:
    plik = open("nie_istnieje.txt", "r")  # Ten plik nie istnieje
except Exception as e:
    print(f"Wystąpił błąd: {e}")  # Wyświetli komunikat błędu
