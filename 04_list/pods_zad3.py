#3▹ Utwórz dowolną tablicę n x n zawierającą dowolny znak,
# a następnie wyświetl jej elementy w formie tabeli n x n.
# Elementy powinny być oddzielone spacją

tab = [['-', '-', '-'],
print(list(tab))
for row in tab:
    print(row[0], row[1], row[2])# join