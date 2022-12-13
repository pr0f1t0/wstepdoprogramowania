def find(lista,  wartość):
    indeksy = []
    a = 0
    for i in lista:
        if i == wartość:
            indeksy.append(a)
        a += 1

    return indeksy

x = find([1, 2, 3, 2, 5, 2, 6], 2)
print(x)

y = find("abacana", "a")
print(y)
