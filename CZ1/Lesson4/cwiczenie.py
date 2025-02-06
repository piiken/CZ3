# Tworzymy listę
dishes = ["pizza", "spaghetti", "sushi"]

# Wyświetlanie listy
print("Twoje ulubione potrawy:")
for dish in dishes:
    print(dish)

# Dodawanie nowej potrawy
new_dish = input("Podaj swoją ulubioną potrawę: ")
dishes.append(new_dish)
print("Zaktualizowana lista potraw:", dishes)

# Usuwanie potrawy
remove_dish = input("Którą potrawę chcesz usunąć? ")
if remove_dish in dishes:
    dishes.remove(remove_dish)
    print("Zaktualizowana lista potraw:", dishes)
else:
    print("Nie znaleziono takiej potrawy na liście.")