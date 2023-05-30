import random

def generate_combinations(imiona_file: str, nazwiska_file: str, liczba_kombinacji: int, output_file: str) -> None:
    imiona = []
    nazwiska = []

    with open(imiona_file, 'r') as file:
        imiona = file.read().splitlines()

    with open(nazwiska_file, 'r') as file:
        nazwiska = file.read().splitlines()

    if liczba_kombinacji > len(imiona) * len(nazwiska):
        print("Podana liczba kombinacji jest większa niż dostępna liczba imion i nazwisk.")
        return

    kombinacje = random.sample([(imie, nazwisko) for imie in imiona for nazwisko in nazwiska], liczba_kombinacji)

    with open(output_file, 'w') as file:
        for imie, nazwisko in kombinacje:
            file.write(f"{imie} {nazwisko}\n")

    print(f"Generowanie {liczba_kombinacji} kombinacji zakończone. Wyniki zapisano do pliku {output_file}.")

imiona_file = "imiona.txt"  
nazwiska_file = "nazwiska.txt"  
liczba_kombinacji = 10  
output_file = "wynik.txt"  
generate_combinations(imiona_file, nazwiska_file, liczba_kombinacji, output_file)
