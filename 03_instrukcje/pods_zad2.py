# Pobierz od użytkownika dowolny tekst.txt i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

txt=input("wpisz tu coś")
length=len(txt)

print(txt[1::2])

for i in range(1,length,2):
    id=txt[i]
    print(i+1,id)
