#Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
#Co wiemy o tych numerach tych kart?

#All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#Wszystkie numery kart Visa zaczynają się od 4. Nowe karty mają 16 cyfr. Stare karty mają 13.

#MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
#Numery MasterCard zaczynają się od numerów 51 do 55 lub od 2221 do 2720. Wszystkie mają 16 cyfr.

#American Express card numbers start with 34 or 37 and have 15 digits.
#Numery kart American Express zaczynają się od 34 lub 37 i mają 15 cyfr.

def can_be_card_number(number):
    if number.isnumeric() and 13 <= len(number) <= 16:
        return True
    else:
        print("Nie to nie jest numer karty :D")
        return False


def is_visa(numer):
    return True if numer[0] == '4' and len(numer) in [13, 16] else False


def is_mastercard(number):
    return True if len(number) == 16 and \
                   (51 <= int(number[0:2]) <= 55 or 2221 <= int(number[0:4]) <= 2720) else False


def is_american_express(number):
    return True if len(number) == 15 and number[0:2] in ['34', '37'] else False


def main():
    card = input("Podaj numer karty ->")
    if can_be_card_number(card):
        if is_visa(card):
            print("To jest karta Visa")
        elif is_mastercard(card):
            print("To jest MasterCard")
        elif is_american_express(card):
            print("To jest AmericanExpress")
        else:
            print("Nie znany numer karty")


# --- main ----
main()




