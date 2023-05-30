import random
from random import randint

def gra_zgadnij_liczbe():
    los=randint(0,100)
    odp=-1
    i=0

    print("Gra zgadnij liczbę od 1 do 100.")

    while odp != los:
        i += 1
        odp = int(input("Podaj liczbę od 1 do 100: "))
        if odp > los:
            print("Wylosowana jest mniejsza od Twojej.")
        elif odp < los:
            print("Wylosowana liczba jest większa od Twojej.")
    print("Odgadłeś liczbę za", i ,"razem.")

    ponowna_gra = input("Czy chcesz zagrać jeszcze raz? (tak/nie): ")
    if ponowna_gra.lower() == "tak":
        gra_zgadnij_liczbe()

gra_zgadnij_liczbe()

