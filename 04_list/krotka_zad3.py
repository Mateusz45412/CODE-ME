#Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby.
# Jeśli liczba znajduje się na krotce wyswietl jej indeks.
my_tumple = (1, 2, 3, 4, 5, 6, 14)
num=int(input("podaj dowolna liczbę"))

# for index in range(len(my_tumple)):
#     if my_tumple[index]==num:
#        print("Index ->", index)

for index, value in enumerate(my_tumple):