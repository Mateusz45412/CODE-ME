# 9▹ Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części.
# W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
#     Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
#             dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
#             ponownie wyświetl zmieniony słownik
#     Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności.
# Dopisz odpowiednie komunikaty.


car = {"marka": "Nissan", "model": "Micra", "rocznik": 1995, "orginal": bool(90 > 75)}
rok2 = int(car['rocznik'])
marka2 = car['marka']
model2 = car['model']
orginal2 = car['orginal']


def rok(year_car, mark, model, orginal):

    difference = 2022-year_car
    if difference >= 25 and orginal is True:
        print(f"“Gratulacje! Twój samochód {mark} {model} może być zarejestrowany jako zabytek")
    elif difference >= 25 and orginal is False:
        print(f"Twój samochód {mark} {model}  ma dobry rocznik ale niestety nie ma min. 75% oryginalnych części\n"
      f" odmowa rejestracji jako zabytek")
    elif difference <= 25 and orginal is True:
        print(f"Twój samochód {mark} {model} jest jeszcze zbyt młody, ale  ma min. 75% oryginalnych części\n"
              f" odmowa rejestracji jako zabytek")
    elif difference <= 25 and orginal is False:
        print(f"Twój samochód {mark} {model} jest jeszcze zbyt młody i nie  ma min. 75% oryginalnych części\n"
              f" odmowa rejestracji jako zabytek")


rok(rok2, marka2, model2, orginal2)
