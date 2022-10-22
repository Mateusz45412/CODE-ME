# Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
#input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
list=[1, 2, 2, 4, 11, 12, 13, 14, 21, 22, 23, 24]

print(list.reverse())
length=len(list)
n3=length//3

n=3
for i in range(length):
    tab = [[list[i]]*n]*n

    for row in tab:
        print(''.join(row))

