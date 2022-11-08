n = int(input("Podaj ilość studentów: "))
i = 1
suma = 0

while True:
    punkty = int(input(f"Proszę podać punkty dla studenta {i}: "))
    if 0 > punkty or punkty > 100:
        print("Niepoprawna liczba punktow")
        continue

    suma += punkty
    i += 1
    if i > n:
        break


średnie = suma / n
print(f"Średnia ocena grupy = {średnie}")



