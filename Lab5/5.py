import random as r
punkty = [round(r.uniform(0, 50), 2) for i in range(15)]
print(punkty)
print(f"Najmniejsza liczba punktów: {min(punkty)}, największa liczba punktów: {max(punkty)}")
x = float(input("Prosze podać liczbę: "))
try:
    x in punkty
    print(punkty.index(x))
except:
    print("Nie ma tej liczby")

avg = sum(punkty)/len(punkty)
print(round(avg, 2))

powyżej = [i for i in punkty if i > avg]
poniżej = [i for i in punkty if i < avg]
print(f"Powyżej: {powyżej}, poniżej: {poniżej}")



