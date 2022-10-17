#Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik,
# w przeciwnym wypadku wyświetl “Koniec”.

liczba1=int(input("podaj liczbe nr 1: "))
liczba2=int(input("podaj liczbe nr 2: "))
suma=liczba1+liczba2
if suma>100:
    print("suma dwóch liczb wynosi",suma)
else:
    print("koniec")