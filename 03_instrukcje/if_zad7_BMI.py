#Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
# która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.
print("Kalkulator BMI")
waga=float(input("Wpisz swoją wage [kg]"))
wzrost=float(input("podaj swoj wzrost [m]"))
BMI=(waga/(wzrost**2))
print("twoje BMI wynosi", round(BMI,2))

if BMI<18:
    print("niedowaga")
elif BMI<=25:
    print("waga prawidłowa")
elif BMI<=30:
    print("nadwaga")
else:
    print("otyłość")