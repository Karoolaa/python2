def dodawanie(a: float,b: float) ->None:
    """Wykonuje dodawanie"""
    return a+b

def odejmowanie(a,b) ->None:
    """wykonuje odejmowanie"""
    return a-b

def mnozenie(a,b) ->None:
    """Wykonuje mnozenie"""
    return a*b

def dzielenie(a,b) ->None:
    if b == 0:
        raise ValueError("Nie mozna dzielic przez 0")
    """Wykonuje dzielenie"""
    return a/b


while True:
    print("Wybierz działanie")
    print("1-dodawanie")
    print("2-odejmowanie")
    print("3-mnozenie")
    print("4-dzielenie")
    print("0-Wyjście")
    """Wyświetla opcje do wybrania"""

    podbranie = input("Wybierz opcje od 0 do 4: ")
    """Pobiera od uytkownika co chce zrobic"""

    if podbranie == "0":
        break
    elif podbranie == "1":
        a = float(input("Podaj pierwsza liczbe: "))
        b = float(input("Podaj druga liczbe: "))
        wynik = dodawanie(a,b)
        print(f"Wynik: {wynik}")
    elif podbranie == "2":
        a = float(input("Podaj pierwsza liczbe: "))
        b = float(input("Podaj druga liczbe: "))
        wynik = odejmowanie(a,b)
        print(f"Wynik: {wynik}")
    elif podbranie == "3":
        a = float(input("Podaj pierwsza liczbe: "))
        b = float(input("Podaj druga liczbe: "))
        wynik = mnozenie(a,b)
        print(f"Wynik: {wynik}")
    elif podbranie == "4":
        a = float(input("Podaj pierwsza liczbe: "))
        b = float(input("Podaj druga liczbe: "))
        try:
            wynik = dzielenie(a,b)
            print(f"Wynik: {wynik}")
        except ValueError as e:
            print(e)
    else:
        print("Zły wybór, spróbuj ponownie")
    
