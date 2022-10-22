from random import randint
print("Aguś witaj w grze CIEPŁO - ZIMNO")
print("masz 6 prób")

los = randint(1, 100)

for i in range(1,8):
    if i ==7:
        print(f"Przegrałaś -  szukana liczba to {los}")
    else:
        traf = int(input("Aguś podaj swoją liczbę z zakresu od 1 do 100: "))
        roznica1 = traf - los
        roznica2 = los - traf
        print(f"r1 {roznica1}")
        print(f"r2 {roznica2}")
        print(los)
        if los == traf:
            print(f"Wygrałaś -  szukana liczba to {los}")
            break

        elif traf>=los:
            if roznica1 <= 10 and roznica1 > 0:
                print(f"Bardzo Ciepło masz jeszcze {6 - i} prób")
            elif roznica1 <= 20 and roznica1 > 10:
                print(f"Bardzo Ciepło masz jeszcze {6 - i} prób")
            elif roznica1 <= 30 and roznica1 > 20:
                print(f"Zimno masz jeszcze {6 - i} prób")
            elif roznica1 <= 100 and roznica1 > 30:
                print(f"Bardzo Zimno masz jeszcze {6 - i} prób")
        elif traf < los:
            if roznica2 <= 10 and roznica2 >0:
                print(f"Bardzo Ciepło masz jeszcze {6 - i} prób")
            elif roznica2 <= 20 and roznica2 >10:
                print(f"Bardzo Ciepło masz jeszcze {6 - i} prób")
            elif roznica2 <= 30 and roznica2 >20:
                print(f"Zimno masz jeszcze {6 - i} prób")
            elif roznica2 <= 100 and roznica2 >30:
                print(f"Bardzo Zimno masz jeszcze {6 - i} prób")
