#  Utwórz dowolną krotkę zawierającą kilka wartości np. 10. Pozwól użytkownikowi podać dowolny index oraz wartość.
#  Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd


items = (1, 0, "string", 22.3,  "lista", 6, 7, 8, 9, (), {'key': 'klucz'}, True, 2//2)
try:
    index = int(input("podaj index"))
    new = input("wpisz cos")
    items[index] = new
    print(items)
    
except TypeError:
    print("TypeError !! Błąd typu")
