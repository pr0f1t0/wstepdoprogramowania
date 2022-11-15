import random as r
zestaw_1 = []
zestaw_2 = []
n = int(input("Podaj liczbę elementów: "))
zestaw_1 = [r.randint(1, 10) for i in range(n)]
zestaw_2 = [r.randint(5, 15) for i in range(n)]
zestaw_3 = zestaw_1 + zestaw_2
#zestaw_3.sort()
print(sorted(zestaw_3)) #sorted() creates a new list and .sort changes the original one

x = int(input("Podaj liczbę: "))
if x in zestaw_1 and zestaw_2:
    print("Liczba z dwóch zestawów")
elif x in zestaw_1:
    print("Liczba z zestawu 1")
elif x in zestaw_2:
    print("Liczba z zestawu 2")
else:
    print("Nie ma takiej liczby w dwóch zestawach")