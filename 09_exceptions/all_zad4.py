# Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku.
# Napisz funkcję, która przyjmie wartości i wyświetli średnią. Program powinen być odporny na błędy użytkownika.
# Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.
def aver(numer):
    list_num = numer.split(",")
    length = len(list_num)
    suma = 0
    for i in list_num:
        suma = suma + int(i)
    print(f"suma liczb {list_num} wynosi {suma}")
    average = suma/length
    print(f"średnia wynosi {average}")

while True:
    num = input(f"podaj liczby po przecinku: ")
    try:
        aver(num)
        break
    except ValueError:
        filename = 'plik.txt'
        with open(filename, 'w', encoding="utf-8") as f:
            f.write('Value Error \n')