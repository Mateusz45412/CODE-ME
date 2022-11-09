#Stwórz listę 10 elementową (różne typy!). Pozwól użytkownikowi podać dowolny index.
# Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.

items = [1, 0, "string", 22.3,  "lista", 6, 7, 8, 9, (), {'key': 'klucz'}, True, 2//2]
try:
    index = int(input("podaj index"))
    result = 1 / items.index(index)
except ValueError:
    print("Błędna wartosć")
except ZeroDivisionError:
    print("nie dziel przez zero")
except TypeError:
    print("Błąd typu")
except IndexError:
    print("Wyszliśmy poza zakres tablicy. Wracaj")

