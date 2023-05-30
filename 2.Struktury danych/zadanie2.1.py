liczby = (10, -3, 4, 9, 12, -6, 0)

najmniejsza = liczby[0]
największa = liczby[0]

for liczba in liczby:
    if liczba < najmniejsza:
        najmniejsza = liczba
    if liczba > największa:
        największa = liczba

print("Najmniejsza liczba: ", najmniejsza)
print("Największa liczba: ", największa)
