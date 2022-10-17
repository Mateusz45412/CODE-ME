#5▹ Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób,
# natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
#     Dorota, Wellman, dziennikarka
#     Adam, Małysz, sportowiec
#     Robert, Lewandowski, piłkarz
#     Krystyna, Janda, aktorka
# Wyświetl w sposób przyjazny dla użytkownika

people=[
    ['Dorota', 'Wellman', 'dziennikarka'],
    ['Adam','Małysz','sportowiec'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka'],
]

# for row in people:
#     print(" ".join(row))

# for row in people:
#     print(row[0], row[1], "-", row[2])

for row in people:
    for col in row:
        if col ==row[-1]:
            print("-",col)
        else:
            print(col, end=" ")
