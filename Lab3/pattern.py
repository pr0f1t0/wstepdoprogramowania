n = int(input("Podaj ilość: "))
for i in range(0, n):

    for j in range(0, i+1):
        print("*", end=" ")

    print("\r")
