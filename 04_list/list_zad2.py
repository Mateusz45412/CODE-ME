# Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

numbers= []
print("10 cyfr")

for i in range(10):
    num=int(input("podaj numer"))
    if not num%2==0:
        numbers.append(num)
print(numbers)