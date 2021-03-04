from typing import List
from student import Student


class Dziennik:
    def __init__(self, rok: int, litera: str):
        self._rok_szkolny: int = rok
        self._ktora_klasa_litera: str = litera
        self._uczniowie: List[Student] = []

    def podaj_ilosc_studentow(self) -> int:
        ilosc_studentow = len(self._uczniowie)
        return ilosc_studentow

    def dodaj_studenta(self, imie, nazwisko):
        id = self._generuj_id()
        s = Student(imie, nazwisko, id)
        self._uczniowie.append(s)

    def _generuj_id(self):
        ...


