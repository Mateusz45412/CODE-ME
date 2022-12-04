import random
girl = ['Susan', 'Lily', 'Emily', 'Sophia', 'Lucy', 'Naomi', 'Julie']
boy = ['Harry', 'Jake', 'Richard', 'Michae', 'Matt', 'John', 'Peter' ]
gender = input("podaj płeć gracza (W/M) ").lower()
breed = ["BLACK", "WHITE"]
def sex():
    if gender == "w":
        nam = random.choice(girl)
        bree = random.choice(breed)
        print(nam, bree)
    elif gender == "m":
        nam = random.choice(boy)
        bree = random.choice(breed)
        print(nam, bree)
    return nam
sex()
