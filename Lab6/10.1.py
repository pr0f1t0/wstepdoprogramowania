import random as r
rand = r.randint(0, 15)

def game():
    tries = 0
    while True:
        a = int(input("Podaj liczbę: "))
        if a != rand:
            tries += 1
            print(f"Nie odgadałeś! Liczba prób: {tries}")
            continue

        else:
            print(f"Wygrałeś! Losowa liczba: {rand}, ilość prób: {tries}")
            break




game()