#2▹ Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

krotka=(1,2,3,4,4,3,2,1,1,1,1,1)
krotkas=set(krotka)
k=list(krotkas)

for i in krotkas:
    x = krotka.count(i)
    print(f" nr {i} występuje {x} razy ")
