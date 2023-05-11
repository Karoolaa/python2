class czytelnik:
    id: int= -1

    def __init__(self,
                 czytelnik_imie: str, czytelnik_nazwisko: str, wiek: int, numer_telefonu: int):
    
        czytelnik.id += 1

        self.id = czytelnik.id
        self.kto = self.stworz_kto(czytelnik_imie, czytelnik_nazwisko)
        self.wiek = wiek
        self.numer_telefonu = numer_telefonu

    def stworz_kto(self, imie: str, nazwisko: str) -> dict[str, str]:
        return {"imie": imie, "nazwisko": nazwisko}