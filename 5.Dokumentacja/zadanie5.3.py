def dodawanie(a: float, b: float) -> float:
    """Wykonuje dodawanie"""
    return a + b

def odejmowanie(a: float, b: float) -> float:
    """Wykonuje odejmowanie"""
    return a - b

def mnozenie(a: float, b: float) -> float:
    """Wykonuje mnożenie"""
    return a * b

def dzielenie(a: float, b: float) -> float:
    """Wykonuje dzielenie"""
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
    
    podbranie: str = input("Wybierz opcję od 0 do 4: ")
    
    if podbranie == "0":
        break
    elif podbranie == "1":
        a: float = float(input("Podaj pierwszą liczbę: "))
        b: float = float(input("Podaj drugą liczbę: "))
        wynik: float = dodawanie(a, b)
        print(f"Wynik: {wynik}")
    elif podbranie == "2":
        a: float = float(input("Podaj pierwszą liczbę: "))
        b: float = float(input("Podaj drugą liczbę: "))
        wynik: float = odejmowanie(a, b)
        print(f"Wynik: {wynik}")
    elif podbranie == "3":
        a: float = float(input("Podaj pierwszą liczbę: "))
        b: float = float(input("Podaj drugą liczbę: "))
        wynik: float = mnozenie(a, b)
        print(f"Wynik: {wynik}")
    elif podbranie == "4":
        a: float = float(input("Podaj pierwszą liczbę: "))
        b: float = float(input("Podaj drugą liczbę: "))
        try:
            wynik: float = dzielenie(a, b)
            print(f"Wynik: {wynik}")
        except ValueError as e:
            print(e)
    else:
        print("Zły wybór, spróbuj ponownie")
