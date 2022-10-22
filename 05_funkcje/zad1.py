#napisz funkcje, która pyta użytkownika o pary książka + ocena i zapisuje je w programie
def add_book():
    title = input ("podaj nazwe książk")
    rate = int(input("podaj ocene książki"))
    list_books.append([title, rate]) #zapisuje

def get_book():
    while True:
        numer=int(input("podaj numer ksiazki: "))
        if 3 >= numer or numer >= 3:
            print("tytul: ", list_book[numer - 1][0], "ocena:", list_book[numer - 1][1])
            break
        else:
            print("numer nie istnieje")


def main():
    list_books = []
    for i in range(3):
        print("Książka",i+1)
        add_book(list_books)
    print(list_books)
    get_book()
