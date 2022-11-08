liczba_str = input("Podaj liczbę: ")
podstawa = int(input("Podaj podstawę: "))
liczba = [int(x) for x in liczba_str]

wynik = 0
el = 0
n = len(liczba)

for i in liczba:
    if any(x >= podstawa for x in liczba):
        print("Niepoprawna liczba przy danej podstawie")
    else:
        for i in range(n):
            a = podstawa ** (n - 1) * liczba[el]
            wynik += a
            n -= 1
            el += 1
print(wynik)
