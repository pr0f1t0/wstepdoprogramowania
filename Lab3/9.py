n = int(input("Podaj ilość: "))
k = n - 1
for i in range(0, n):

    for j in range(0, k):
        print(" ", end="")


    for d in range(0, i+1):
        print("*", end="")

    print("\r")