# Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
# Program zacznie ze stworzonym słownikiem o trzech kluczach:
#             marka (str)
#             model (str)
#             rocznik (int)
# Wypisze ten słownik na ekran (bez żadnego formatowania)
# Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
# “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
# Jeśli nie spełnia powyższego warunku, wypisze komunikat:
# “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
# Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!),
# aby zobaczyć, czy progam również zmienia swoje zachowanie.

car = {"marka": "Nissan", "model": "Micra", "rocznik": 1995}
rok2 = int(car['rocznik'])
marka2 = car['marka']
model2 = car['model']


def rok(year_car, mark, model):

    difference = 2022-year_car
    if difference >= 25:
        print(f"“Gratulacje! Twój samochód {mark} {model} może być zarejestrowany jako zabytek")
    else:
        print(f"Twój samochód {mark} {model}  jest jeszcze zbyt młody")


rok(rok2, marka2, model2)



