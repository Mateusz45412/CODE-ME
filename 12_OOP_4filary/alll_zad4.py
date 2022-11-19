#4▹ Utwórz klasę zegaro-kalendarza. Zegaro-kalendarza łączy cechy zegara oraz kalendarza.
# Zaimplementuj dziedziczenie wielokrotne. Nasz zegaro-kalendarza powinen móc podawać aktualną datę
# oraz wyświetlać ile dni ma dany miesiąc. Dodatkowo utwórz sposób wyświetlania tak, aby zegaro-kalendarz zawierał datę,
# godzinę oraz widok dni ułożonych tygodniowo.
# Dla uproszczenia przyjmij 7 dni w tygodniu zawsze zaczyna się od pierwszego dnia
from datetime import date, datetime, time
class Date:
    def __init__(self, data):
        self.data = data
        print("data")
        print(date.today())

class Time:
    print("godzina")
    print(datetime.today())


class ZegaroKalendarz(Date, Time):
    print("Zegaro - Kalendarz")


