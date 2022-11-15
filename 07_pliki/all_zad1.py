# Utwórz plik zawierający listę ok. 20 cytatów. Każdy cytat powinen się znaleźć w nowej linii.
#Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś. Np. można wyświetlić tak:
# Quote of the day is:
#
# **************************************
#            be or not to be?
# **************************************

#     zmodyfikuj plik źródłowy, tak aby użytkownik mógł podać własną nazwę pliku z cytatami
#     plik z cytatami powinen również zawierać informację o autorze, wyświetl cytat i pod spodem autora

import random


def open_file():
    filename = input("Give me file name ...")
    with open(filename) as file:
        return file.readlines()


def get_random_quote(list_of_quotes):
    return random.choice(list_of_quotes).strip()


def show(quote):
    print("Quote of the day is:\n")
    txt, author = quote.split(' -')

    print('*' * 100)
    print(txt.center(100))
    print(author.center(100))
    print('*' * 100)


def main():
    quotes = open_file()
    quote = get_random_quote(quotes)

    show(quote)


main()

# import random
#
#
# filename = 'cytat.txt'
# with open(filename, 'r', encoding="utf-8") as f:
#     content = f.readlines()
#
# kwybor = random.choice(content).strip()
# print("Quote of the day is\n")
# print(('*')*70)
# print(kwybor.center(70))
# print(('*')*70)
