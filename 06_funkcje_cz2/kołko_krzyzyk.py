import random

list = ["|", "a1b1", "|", "a1b2", "|", "a1b3", "|", "\n"
        "|", "a2b1", "|", "a2b2", "|", "a2b3", "|", "\n"
        "|", "a3b1", "|", "a3b2","|", "a3b3", "|"]

list_comp = ["a1b1", "a1b2", "a1b3", "a2b1", "a2b2", "a2b3", "a3b1", "a3b2", "a3b3"]
sign = input("Co wybierasz kółko czy krzyzyk ?? o/x ")
see = ("  " + sign + " ")

if sign == "o":
    sign_comp = "x"
else:
    sign_comp = "o"
see_comp = ("  " + sign_comp + " ")

wyg = see*3
wyg_comp = see_comp*3


def win(you, comp):
    if (list[1] + list[3] + list[5]) == you:
        return True
    elif (list[1] + list[3] + list[5]) == comp:
        return False
    if (list[8] + list[10] + list[12]) == you:
        return True
    elif (list[8] + list[10] + list[12]) == comp:
        return False
    if (list[-6] + list[-4] + list[-2]) == you:
        return True
    elif (list[-6] + list[-4] + list[-2]) == comp:
        return False
    if (list[1] + list[8] + list[-6]) == you:
        return True
    elif (list[1] + list[8] + list[-6]) == comp:
        return False
    if (list[3] + list[10] + list[-4]) == you:
        return True
    elif (list[3] + list[10] + list[-4]) == comp:
        return False
    if (list[5] + list[12] + list[-2]) == you:
        return True
    elif (list[5] + list[12] + list[-2]) == comp:
        return False
    if (list[1] + list[10] + list[-2]) == you:
        return True
    elif (list[1] + list[10] + list[-2]) == comp:
        return False
    if (list[5] + list[10] + list[-6]) == you:
        return True
    elif (list[5] + list[10] + list[-6]) == comp:
        return False


def main():
    while(1):
        win(wyg, wyg_comp)
        print(*list)
        if win(wyg, wyg_comp) == None:
            ruch = input("Jaki jest twój ruch ").lower()

            list_comp.remove(ruch)
            indeks = list.index(ruch)

            computer = random.choice(list_comp)  # computer
            indeks_comp = list.index(computer)  # computer

            ruch = list[indeks]
            list[indeks] = see

            computer = list[indeks_comp]  # computer
            list_comp.remove(computer)
            list[indeks_comp] = see_comp
        elif win(wyg, wyg_comp) == True:
            print("Koniec GRY WYGRYWASZ !!")
            break
        elif win(wyg, wyg_comp) == False:
            print("Koniec GRY WYGRYWA KOMPUTER !!")
            break
main()