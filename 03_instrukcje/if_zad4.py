# Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

znaki=input("wprowadź dowolne znaki :)")
dlugosc=len(znaki)
if dlugosc>5:
    znaki=znaki.replace("a","z")
    znaki=znaki.replace("A","Z")
    print(znaki)
else:
    print("string jest krótszy niż 5 znaków")