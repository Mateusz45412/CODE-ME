# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie
# (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.
print("musi zgadnąć liczbę od 0 - 20 ukrytą w programie")
secret_num = 5
num=int(input("podaj liczbe "))
while not num==secret_num:
    print("PUDŁO !!")
    num = int(input("podaj liczbe"))
print(f"gratulacje ukryta liczba to {num}")