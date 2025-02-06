try:
    plik = open("dane.txt", "r")
    zawartosc = plik.read()
except FileNotFoundError:
    print("Plik nie istnieje!")
finally:
    print("Ten kod wykona się zawsze, niezależnie od błędów.")  
