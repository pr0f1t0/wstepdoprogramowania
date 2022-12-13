def dodawanie(*args):
    res = 0
    for i in args:
        res += i
    return res

def odejmowanie(w1, w2):
    res = w1 - w2
    return res

def mnożenie(*args):
    res = 0
    for i in args:
        res *= i
    return res
def dzielenie(w1, w2):
    if w2 != 0:
        res = w1/w2
        return res
    else:
        return "Dzielenie na 0!"

d = {'+': dodawanie, '-': odejmowanie, '*': mnożenie, '/': dzielenie}
w1 = int(input("Pierwsza liczba: "))
w2 = int(input("Druga licba: "))
działanie = input("Działanie: +, -, * lub /: ")
print(d[działanie](w1, w2))

