def dodawanie(a, b):
    """
    Dodaje dwie liczby i zwraca wynik.
    """
    return a + b


def odejmowanie(a, b):
    """
    Odejmuje drugą liczbę od pierwszej i zwraca wynik.
    """
    return a - b


def mnozenie(a, b):
    """
    Mnoży dwie liczby i zwraca wynik.
    """
    return a * b


def dzielenie(a, b):
    """
    Dzieli pierwszą liczbę przez drugą i zwraca wynik.
    Rzuca wyjątek ValueError, jeśli druga liczba wynosi 0.
    """
    if b == 0:
        raise ValueError("Nie można dzielić przez 0")
    return a / b


while True:
    print("Wybierz działanie")
    print("1 - dodawanie")
    print("2 - odejmowanie")
    print("3 - mnożenie")
    print("4 - dzielenie")
    print("0 - Wyjście")

    podbranie = input("Wybierz opcję od 0 do 4: ")

    if podbranie == "0":
        break
    elif podbranie == "1":
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        wynik = dodawanie(a, b)
        print(f"Wynik: {wynik}")
    elif podbranie == "2":
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        wynik = odejmowanie(a, b)
        print(f"Wynik: {wynik}")
    elif podbranie == "3":
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        wynik = mnozenie(a, b)
        print(f"Wynik: {wynik}")
    elif podbranie == "4":
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        try:
            wynik = dzielenie(a, b)
            print(f"Wynik: {wynik}")
        except ValueError as e:
            print(e)
    else:
        print("Zły wybór, spróbuj ponownie")

