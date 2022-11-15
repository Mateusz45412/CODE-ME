#Stwórz własną implementację kolejki FIFO. Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
# Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki, sprawdzenie czy jest pusta,
# dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).

class Queue:
    def __init__(self, fifo):
        self.fifo = fifo

    def __str__(self):
        return f"FIFO: {self.fifo}"

    def is_empty(self):
        return len(self.fifo) == 0

    def put(self, item):
        self.fifo.append(item)
        print(f"Dodano element {item}!")

    def get(self):
        return self.fifo.pop(0)


kolejka = Queue([3, 5, 6, 6, 7])

print(kolejka)
print(kolejka.is_empty())
kolejka.put(0)
print(kolejka)
print(kolejka.get())
print(kolejka)