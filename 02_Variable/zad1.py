#Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.
#Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.

print("koszt wyprawy")
spalanie_100=float(input("ile na 100km spala twoje auto"))
trasa=float(input("ile przejechałeś km ??"))
cena=float(input("podaj koszt benzyny za 1 litr"))
wynik=((trasa*spalanie_100)/100)*cena
result=cena*trasa/100*spalanie_100
print("Cena całkowita trasy 120 km",round(wynik,2))
print("Cena całkowita trasy 120 km",round(result,2))