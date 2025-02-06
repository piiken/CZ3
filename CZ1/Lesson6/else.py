try:
    liczba = int(input("Podaj liczbę: "))
    wynik = 10 / liczba
except ZeroDivisionError:
    print("Nie dziel przez zero!")
except ValueError:
    print("To nie jest liczba!")
else:
    print(f"Wynik: {wynik}")  # Wykona się tylko, jeśli nie było błędu
finally:
    print("Zakończenie operacji.")  
