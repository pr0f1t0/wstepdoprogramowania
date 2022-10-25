n = int(input("Podaj ilość studentów: "))
i = 1
suma = 0
while i <= n:
    punkty = int(input(f"Proszę podać punkty dla studenta {i}: "))
    suma += punkty
    i += 1
średnie = suma / n
print(f"Średnia ocena grupy = {średnie}")

