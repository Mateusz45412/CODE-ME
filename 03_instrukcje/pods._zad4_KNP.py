# Napisz grę - kamień (k) / papier (p) / nożyce (n).
        # Użytkownik podaje jedną z 3 figur.
        # Komputer losuje jedną z 3 figur.
        # Sprawdź kto wygrał tę rundę.
        # Zmień kod tak, by użytkownik mógł podac liczbę rund.
        # Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
        # Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

import random
print("GRA - KAMIEŃ NOŻYCE PAPIER")
lista = ("papier", "kamień", "nożyce")
wybor = input("\n wpisz swój wybór ")
kwybor = random.choice(lista)
print(f"Twój wybór: {wybor} przeciwko {kwybor}  ")

# while Tpunkty==3 or kpunkty==3:
if wybor==kwybor:
    print("remis")
elif wybor=="kamień" and kwybor=="papier":
    print("wygrywa papier punkt dla komputera")
elif wybor=="papier" and kwybor=="kamień":
    print("wygrywa papier punkt dla Ciebie")

elif wybor=="papier" and kwybor=="nożyce":
    print("wygrywają nożyce punkt dla komputera")
elif wybor=="nożyce" and kwybor=="papier":
    print("wygrywają nożyce punkt dla Ciebie")

elif wybor=="kamień" and kwybor=="nożyce":
    print("wygrywa kamień punkt dla Ciebie")
elif wybor=="nożyce" and kwybor=="kamień":
    print("wygrywają nożyce punkt dla komputera")