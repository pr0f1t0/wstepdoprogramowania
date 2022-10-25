a = int(input("Podaj liczbę pierwszą: "))
b = int(input("Podaj liczbą drugą: "))
if b > a:
    a, b = b, a
while a >= b:
    if b % 2:
        print(b, end=" ")
        b += 1;
        continue


