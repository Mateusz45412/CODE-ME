#1▹ Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek. Każda z nich powinna dziedziczyć z nadrzędnej klasy Ssaki.
# Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta. Utwórz obiekty klas - kot, pies i człowiek,
# udowodnij, że rzeczywiście korzystają z klas rodziców.

class Ssaki:
    def __init__(self, name, budowa, warstwa):
        self.name = name
        self.budowa = budowa
        self.warstwa = wartswa
        print(f"Ssaki typu{name} mają budowę {budowa}, a na zewnątrz pokryte są {warstwa} ")

class Cat(Ssaki):


class Dog(Ssaki):


class People(Ssaki):
