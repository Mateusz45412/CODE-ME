#Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika
# jest podzielna przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

liczba=float(input("podaj liczbe"))
if liczba % 3 == 0:
   print("twoja liczba jest podzielna przez 3")