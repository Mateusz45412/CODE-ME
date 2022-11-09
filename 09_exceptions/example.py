user_value = input("Podaj liczbę od 1 do 100")
# ...
user_value = int(user_value)

number = user_value / 4
user_value = input("Podaj liczbę od 1 do 100")
# .....
while True:
    if user_value.isnumeric():
        user_value = int(user_value)
        break

user_value = int(user_value)

number = user_value / 4
print(f" Number = { number }")
