#Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.
print("witaj")
n1=int(input("wprowadz liczbe nr 1: "))
n2=int(input("wprowadz liczbe nr 2: "))
n3=int(input("wprowadz liczbe nr 3: "))

if n1>=n2>=n3:
 print(n1,n2,n3)
elif n1>=n3>=n2:
 print(n1,n3,n2)

elif n2>=n3>=n1:
 print(n2,n3,n1)
elif n2>=n1>=n3:
 print(n2,n1,n3)

elif n3 >= n2 >= n1:
 print(n3, n2, n1)
elif n3 >= n1 >= n2:
 print(n3, n1, n2)