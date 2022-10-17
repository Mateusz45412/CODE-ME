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
tpunkty = 0
kpunkty = 0

while not tpunkty>=3 or kpunkty>=3:
    if tpunkty==3:
        print("Wygrałeś")
    elif kpunkty==3:
        print("Przegrałeś")
    wybor = input("\n wpisz swój wybór ")
    kwybor = random.choice(lista)
    print(f"Twój wybór: {wybor} przeciwko {kwybor}  ")
    if wybor == kwybor:
        print("remis")
        tpunkty += 1
    elif wybor == "kamień" and kwybor == "papier":
        print("wygrywa papier punkt dla komputera")
        kpunkty += 1
    elif wybor == "papier" and kwybor == "kamień":
        print("wygrywa papier punkt dla Ciebie")
    elif wybor == "papier" and kwybor == "nożyce":
        print("wygrywają nożyce punkt dla komputera")
        kpunkty += 1
    elif wybor == "nożyce" and kwybor == "papier":
        print("wygrywają nożyce punkt dla Ciebie")
        tpunkty += 1
    elif wybor == "kamień" and kwybor == "nożyce":
        print("wygrywa kamień punkt dla Ciebie")
        tpunkty += 1
    elif wybor == "nożyce" and kwybor == "kamień":
        print("wygrywają nożyce punkt dla komputera")
        kpunkty += 1
