#Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
# Napisz rozwiązanie zarówno z użyciem pętli while jak i for.

fahr=int(input('podaj temperature w stopniach Fahrenheita'))
while fahr<=200:
    celc=(5/9)*(fahr-32)
    celc = round(celc,2)
    print(f"{fahr}st Fahrenheit'a -> {celc} st C")
    fahr+=20

#for fahre in range (0, 201, 20):
#    celc=(5/9)*(fahr-32)
#    celc = round(celc,2)
#    print(f"{fahr}st Fahrenheit'a -> {celc} st C")