import library

def test_add_book():
    """Test dodawania książki"""
    result = library.add_book("Testowa książka", "Testowy Autor")
    assert "została dodana" in result

def test_remove_book():
    """Test usuwania książki"""
    library.add_book("Do usunięcia", "Anonim")
    result = library.remove_book("Do usunięcia")
    assert "została usunięta" in result

def test_edit_book():
    """Test edycji autora książki"""
    library.add_book("Edytowana książka", "Stary Autor")
    result = library.edit_book("Edytowana książka", "Nowy Autor")
    assert "Zmieniono autora" in result

def test_find_book():
    """Test wyszukiwania książki"""
    library.add_book("Szukana książka", "Autor")
    result = library.find_book("Szukana książka")
    assert "Szukana książka" in result
