class czytelnik:
    id: int= -1

    def __init__(self,
                 czytelnik_imie: str, czytelnik_nazwisko: str, wiek: int, numer_telefonu: int):
    
        czytelnik.id += 1

        self.__id = czytelnik.id
        self.__kto = self.stworz_kto(czytelnik_imie, czytelnik_nazwisko)
        self.__wiek = wiek
        self.__numer_telefonu = numer_telefonu

    def stworz_kto(self, imie: str, nazwisko: str) -> dict[str, str]:
        return {"imie": imie, "nazwisko": nazwisko}
    
    def pobierz_id(self) -> int:
        return self.__id
    
    def pobierz_czytelnika(self) -> dict[str, str]:
        return self.__kto
    
    def pobierz__wiek(self) -> int:
        return self.__wiek
    
    def pobierz_numer(self) -> int:
        return self.__numer_telefonu