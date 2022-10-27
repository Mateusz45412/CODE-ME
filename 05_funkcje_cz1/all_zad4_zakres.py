# ▹Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
#  Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def add_num(n1, n2, n):
    for i in range(n1, n2):
        if (n < n2) and (n > n1):
            print(f"liczba {n} znajduje się w zadanym zakresie")
            break
        else:
            print(f"liczba {n} jest z poza zakresu")
            break


def main():
    print("Podaj zakres liczb")
    num1 = int(input("Pierwsza liczba zakresu: "))
    num2 = int(input("Ostatnia liczba zakresu: "))
    num = int(input("Podaj liczbę: "))
    add_num(num1, num2, num)


main()