#Skorzystaj ze swojego kodu bmi.py.
# Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika
# oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość)
# w zależności od otrzymanego parametru.
# --- calculate bmi  state
print("Kalkulator BMI")
def calculate():
    waga = float(input("Wpisz swoją wage [kg]"))
    wzrost = float(input("podaj swoj wzrost [m]"))
    bmi = (waga/(wzrost**2))
    print("twoje BMI wynosi", round(bmi, 2))
    return bmi


def get_bmi_state(bmi_value):
    if bmi_value < 18:
        return "niedowaga"
    elif bmi_value <= 25:
        return "waga prawidłowa"
    elif bmi_value <= 30:
        return "nadwaga"
    else:
        return "otyłość"
# -- main --


result_bmi = calculate()
print(get_bmi_state(result_bmi))
