age = int(input("Podaj wiek: "))
if age < 4:
    print("Bilet bezpłątny")
elif age > 18:
    print("Bilet kosztuje 20 zł")
else:
    print("Bilet kosztuje 10 zł")