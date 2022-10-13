#Do zmiennej quote przypisz zdanie:
# „Honesty is the first chapter in the book of wisdom.”, a następnie:
quote="Honesty is the first chapter in the book of wisdom."
#Policz wszystkie znaki w napisie
print("wszystkie znaki w napisie", len(quote))
#Nie modyfikując zmiennej wyświetl słowo wisdom
print(quote[-7:-1])
#Wyświetl tylko pierwszą połowę tekstu
print(quote[0:len(quote)//2])
#Wyświetl tylko kropkę
print(quote[-1])
#Wyświetl od połowy tylko co trzecią literę cytatu
print(quote[len(quote)//2::3])
#Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print(quote[::2])
#Wyświetl cały cytat odwrotnie
print(quote[::-1])
#Zamień wisdom na słowo friendship
print(quote.replace('wisdom','friendshp'))