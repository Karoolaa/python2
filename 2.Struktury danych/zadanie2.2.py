slowo = input("Podaj slowo: ")

odwrocone_slowo = slowo[::-1]
if slowo == odwrocone_slowo:
    print("Słowo jest palindromem.")
    pass
else:
    print("Słowo nie jest palindromem.")
