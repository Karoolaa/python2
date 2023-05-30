class Pojazd:
    def __init__(self, marka, rok_produkcji):
        self.marka = marka
        self.rok_produkcji = rok_produkcji
        self.czy_wypozyczony = False

    def wypozycz(self):
        if not self.czy_wypozyczony:
            self.czy_wypozyczony = True
            print("Pojazd został wypożyczony.")
        else:
            print("Pojazd jest już wypożyczony.")

    def oddaj(self):
        if self.czy_wypozyczony:
            self.czy_wypozyczony = False
            print("Pojazd został zwrócony.")
        else:
            print("Pojazd jest już dostępny.")

    def informacje(self):
        print("Marka:", self.marka)
        print("Rok produkcji:", self.rok_produkcji)
        print("Status:", "Wypożyczony" if self.czy_wypozyczony else "Dostępny")


class Jednoslad(Pojazd):
    def __init__(self, marka, rok_produkcji, rodzaj):
        super().__init__(marka, rok_produkcji)
        self.rodzaj = rodzaj


class Wieloslad(Pojazd):
    def __init__(self, marka, rok_produkcji, liczba_kol):
        super().__init__(marka, rok_produkcji)
        self.liczba_kol = liczba_kol



jednoslad = Jednoslad("Rowerek", 2022, "Rower")
jednoslad.informacje()
jednoslad.wypozycz()
jednoslad.wypozycz()
jednoslad.oddaj()

print()

wieloslad = Wieloslad("Samochód", 2020, 4)
wieloslad.informacje()
wieloslad.wypozycz()
wieloslad.oddaj()