wiek =int(input("Podaj wiek: "))
kategoria =input("Podaj kategorie prawa jazdy jaka posiadasz: ")
ile =int(input("Podaj ile lat masz kategorie A2: "))
kategoria2="A2"

if wiek >= 24:
    print("Mozesz robic prawo jazdy A")
    pass
elif wiek <= 24 and wiek >= 20 and ile >= 2 and kategoria == kategoria2:
    print("Mozesz robic prawo jazdy")
    pass
else:
    print("Nie mozesz")