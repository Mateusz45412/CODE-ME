# Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
tytul=input("prosze podac tytuł ksiżki")
nazwisko=input("prosze podac nazwisko autora")
strony=input("prosze podac liczbę stron")
# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
print("strony są tylko liczbami",strony.isdigit())
print("nazwisko składa sie tylko z liter",nazwisko.isalpha())
print("tytuł składa sie tylko z liter",tytul.isalpha())
# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
print("Tutuł:",tytul.capitalize())
print("Nazwisko",nazwisko.capitalize())
# Połącz dane w jeden ciąg book za pomocą spacji
print("Połącz dane w jeden ciąg book za pomocą spacji")
print(tytul+nazwisko+strony)
# Policz liczbę wszystkich znaków w napisie book
print(len("book"))