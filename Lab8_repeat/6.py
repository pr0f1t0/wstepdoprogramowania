import random as rn
def gra():
    x = rn.randint(0, 20)
    tries = 0
    while True:
        tries += 1
        y = int(input("Podaj liczbę: "))
        if x == y:
            print(f"Wygrałeś! Liczba prób: {tries}")
        elif x > y:
            print(f"Wylosowana liczba jest mniejsza! Liczba prób: {tries}")
        else:
            print(f"Wylosowana liczba jest większa! Liczba prób: {tries}")

gra()

