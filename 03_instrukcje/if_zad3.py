#Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
# Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry,
# ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

opinia1=int(input("podaj opinie od 1-10"))
opinia2=int(input("podaj opinie od 1-10"))
opinia3=int(input("podaj opinie od 1-10"))
sr=(opinia1+opinia2+opinia3)/3
print("średnia opinia o książce wynosi ",sr)
if sr>7:
    print("Bardzo dobra książka")
elif sr>=5:
    print("przeciętna")
else:
    print("nie warta uwagi")
