import math

class FiguraGeometryczna:
    def oblicz_pole(self):
        pass

    def oblicz_obwod(self):
        pass


class Kwadrat(FiguraGeometryczna):
    def __init__(self, bok):
        self.bok = bok

    def oblicz_pole(self):
        return self.bok ** 2

    def oblicz_obwod(self):
        return 4 * self.bok


class Kolo(FiguraGeometryczna):
    def __init__(self, promien):
        self.promien = promien

    def oblicz_pole(self):
        return math.pi * self.promien ** 2

    def oblicz_obwod(self):
        return 2 * math.pi * self.promien


kwadrat = Kwadrat(5)
print("Pole kwadratu:", kwadrat.oblicz_pole())
print("Obwód kwadratu:", kwadrat.oblicz_obwod())

kolo = Kolo(3)
print("Pole koła:", kolo.oblicz_pole())
print("Obwód koła:", kolo.oblicz_obwod())