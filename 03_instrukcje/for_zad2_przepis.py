#Utwórz listę, która zawiera składniki na ulubione danie.
# Wyświetl komunikaty co należy pokolei dodać.
# Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.
skladniki=input("wpisz trzy składniki na ulubione danie odzielone spacją")
skladniki=skladniki.split()
length=len(skladniki)
print("lista składników na ulubione danie")

for i in range(length):
    print(i,skladniki[i],"\n")

for i in range(length):
    print(i+1,skladniki[i],"wymieszać z",skladniki[i-1],)

print("\n Piec jedną blachę po drugiej, w nagrzanym piekarniku ok. 12 minut w temperaturze 180°C, ")
print("Po upieczeniu pozostawić do ostygnięcia.")
