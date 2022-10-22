#Skorzystaj ze swojego kodu bmi.py.
# Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika
# oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość)
# w zależności od otrzymanego parametru.

# --- calculate bmi  state

print("Kalkulator BMI")
def licz():
    waga=float(input("Wpisz swoją wage [kg]"))
    wzrost=float(input("podaj swoj wzrost [m]"))
    bmi=(waga/(wzrost**2))
    print("twoje BMI wynosi", round(BMI,2))
    return bmi

licz()
def wartosc(licz):
    if bmi<18:
    print("niedowaga")
    elif bmi<=25:
    print("waga prawidłowa")
    elif bmi<=30:
         print("nadwaga")
    else:
print("otyłość")