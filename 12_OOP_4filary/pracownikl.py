class Pracownik:
    firma = "Infor"

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def wynagrodzenie(self):
        return f"{self.firstname} {self.lastname} w firmie {self.firma} zarabia 4000 zł"

class Ksiegowy(Pracownik):

    pracownik_A = Pracownik("Anna", "Nowak", 23)
    pracowmnik_B = Pracownik("Bartek", "Kowal", 24)

print("Mam na imię:", student_A.firstname + ' ' + student_A.lastname)
print(student_A.email())
print(student_B.email())

student_A.lastname = "Smith"
print("Mam na imię:", student_A.firstname + ' ' + student_A.lastname)


