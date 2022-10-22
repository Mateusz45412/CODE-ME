#Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

numbers=[]
print("podaj 8 liczb")

for i in range(8):
    num=int(input(f"podaj liczbę nr {i+1} "))
    numbers.append(num)
print(numbers[:])
if numbers[5]==numbers[6]:
    print(f"{numbers[5]}={numbers[6]} a więc 2 środkowe elementy są takie same")
elif not numbers[5]==numbers[6]:
    print(f"{numbers[5]} i {numbers[6]} są różne a więc 2 środkowe elementy nie są takie same")

# print(f"{s1},={s2} a więc 2 środkowe elementy są takie same")