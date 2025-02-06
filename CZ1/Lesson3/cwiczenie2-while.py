while True:
    l = int(input("Podaj liczbę"))
    if l > 0:
        break #kończy pentlę jeśli liczba większa od 0
    print("Liczba musi być >0")

for i in range(1, l+1):
    print(f"Liczba: {i}")