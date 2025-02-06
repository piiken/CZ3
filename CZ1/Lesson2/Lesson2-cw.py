#Program pyta o wiek i określa czy jest pełnoletni <, =, >
wiek = int(input("Ile masz lat?"))
if wiek > 18:
    print("Masz więcej niż 18 lat.")
elif wiek == 18:
    print("Masz równe 18 lat.")
else:
  print("Nieprawidłowe dane")