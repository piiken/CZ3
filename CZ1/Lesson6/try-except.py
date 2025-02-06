try:
    # Kod, który może spowodować błąd
    liczba = int(input("Podaj liczbę: "))
    wynik = 10 / liczba  # Jeśli użytkownik poda 0, pojawi się błąd
    print(f"Wynik: {wynik}")
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")
except ValueError:
    print("Podana wartość nie jest liczbą!")
