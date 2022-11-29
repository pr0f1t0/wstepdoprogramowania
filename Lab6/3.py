'''def wyswietl(*args):
    m = args[0]
    for i in args[1:]:
        if i > m:
            m = i

    return m


print(wyswietl(5,7,76,0,8.56))
print(wyswietl(2,6,-2))
x = wyswietl(100,2,6,7,8,9,0,5,55)
print(x)'''


'''def wyswietl(*args):
    if len(args) == 0:     
        return 
    m = args[0]
    for i in args[1:]:
        if i > m:
            m = i

    return m'''

def wyswietl(num1, *args):
    m = num1
    for i in args:
        if i > m:
            m = i

    return m
x = wyswietl(1, 1873823, 1066)
print(x)


