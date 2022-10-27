#2▹ Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb.
# minimum_of(a, b, c).

# def min_of():
#     if a < b < c or b < a < c:
#         return a
#     elif b < c < a or b < a < c:
#         return b
#     else:
#         return c
# # main
# a = int(input("podaj liczbę nr 1-."))
# b = int(input("podaj liczbę nr 2-."))
# c = int(input("podaj liczbę nr 3 -."))
# result = min_of()
# print(result)

def min_of_2(x, y):
    return x if x < y else y


def min_of_3(a, b, c):
    min_value = min_of_2(a, b)
    return min_of_2(min_value, c)


# main
a = int(input("podaj liczbę nr 1-."))
b = int(input("podaj liczbę nr 2-."))
c = int(input("podaj liczbę nr 3 -."))
result = min_of_3(a, b, c)
print(result)
