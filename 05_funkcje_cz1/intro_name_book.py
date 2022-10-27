#Napisz funkce która zapyta o numer książki i wyświetli tytuł wraz z oceną.
# def nr_book():
#     list_books = ["THG", "Python", "Coś"]
#     o_books = [5, 4, 3]
#     rate = int(input("podaj numer książki"))
#     print(list_books[rate], "ma ocene", o_books[rate])
# nr_book()

def add_book():
    title = input ("podaj nazwe książk")
    rate = int(input("podaj ocene książki"))
    list_books.append([title, rate]) #zapisuje


#main
list_books =[]
for i in range(3):
    print("Książka", i + 1)
    add_book()
print(list_books)


