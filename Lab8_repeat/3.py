def potęga(lista_l, lista_p):
    l = []
    if len(lista_l) != len(lista_p):
        print("Niepoprawne rozmiary list")
        return ''
    else:
        for i in range(len(lista_l)):
            l.append(lista_l[i]**lista_p[i])

    return l

lista1 = [1, 2, 3]
lista2 = [4, 3, 2, 1]
p = potęga(lista1, lista2)
print(p)



