#Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy,
# utwórz nowy łańcuch s3, dołączając s2 w środku s1.
s1=(input("podaj 1 wyraz "))
s2=(input("podaj 2 wyraz "))
lenght=len(s1)
index_center = lenght//2
s3= s1[:index_center]+s2+s1[index_center:]
print(s3)