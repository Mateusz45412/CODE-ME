#Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry.
# Wyświetl nazwę właśnie spakowanego przedmiotu,
# po ostatnim przedmiocie pokaż informację: “Great, we are ready!”
items=input("wpisz listę przedmiotów, które zabierzesz na samotną wyprawę w góry ")
items=items.split()
lenght=len(items)
for i in range (lenght):
    print(i," ",items[i])
print("Great, we are ready!")