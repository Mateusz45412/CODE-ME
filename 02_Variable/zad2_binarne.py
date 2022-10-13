# Na kartce papieru oblicz jak twój wiek będzie reprezentowany binarnie.
# Sprawdź czy to samo zwróci Python.
# Dla podanej liczby w systemie dwójkowym bin_num = 1001111 oblicz wartość w systemie dziesiętnym.
# Zamianę z systemu binarnego na dziesiętny napisz samodzielnie (nie korzystaj z metody wbudowanej).
# Dla liczb hex_num = 1DB i oct_num = 2063 zwróć wartość w systemie dziesiętynym.
wiek=int(input("ile masz lat ?"))
w1=wiek//2 #wynik1
r1=wiek%2  #reszta1
w2=w1//2
r2=w1%2
w3=w2//2
r3=w2%2
w4=w3//2
r4=w3%2
w5=w4//2
r5=w4%2
w6=w5//2
r6=w5%2
w7=w6//2
r7=w6%2
print("WOW masz juz 0b ->",r7,r6,r5,r4,r3,r2,r1,"lat !!")
print("WOW masz juz",(bin(wiek)),"lat !!")
print("WOW masz juz",(oct(wiek)),"lat !!")
print("WOW masz juz",(hex(wiek)),"lat !!")