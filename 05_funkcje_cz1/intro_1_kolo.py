#1▹ Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.
# def pole_kola():
#     r = int(input("podaj promień kola"))
#     pole=3.14*r*r
#     print(pole)
# pole_kola()

def calc_circle_area(radious):
    pi = 3.14
    result = pi * (radious ** 2)
    print(result)


#---main
calc_circle_area(10)
calc_circle_area(5)
calc_circle_area(2.5)