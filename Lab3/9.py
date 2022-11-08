n = int(input("Podaj ilość: "))
k = n - 1
for i in range(0, n):

    for d in range(0, i+1):
        print("*", end="")

    for j in range(0, k):
        print(" ", end=" ")

    k -= 1

    print("\r")