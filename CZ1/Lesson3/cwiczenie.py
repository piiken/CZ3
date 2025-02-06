#pytanie urzytkownika o długość pętli (ile liczb)
l = int(input("Wprowadz liczbe"))
if l < 1:
    print("Podaj liczbę dodatnią")
else:
    for i in range(1, l+1):
        print(f"Liczba: {i}")
