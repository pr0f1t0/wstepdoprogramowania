import math

while True:
    op = input(
        "Podaj operację (+, -, /, *, **, root, % lub log)\nNapisz 'Help' żeby otrzymać informację o operacjach lub 'Stop' żeby "
        "wyłaczyć program : ")
    if op == "Help":
        print(
            "+ — dodawanie\n- — odejmowanie (argument 1 - argument 2\n/ — podział (argument 1 / argument 2)\n* — mnożenie\n"
            "** — potęga(argument 1 ** argument 2)\nroot — pierwiastek (argument 1 - stompień pierwiastka, argument 2 - liczba)\n"
            "% — reszta od podziału(argument 1 % argument 2)\nlog - logarytm (argument 1 - podstawa, argument 2 - liczba logarytmowana)")
        continue
    else:
        if op == "Stop":
            print("Dziękuje za korzystanie.")
            break
        arg1 = float(input("Podaj argument 1: "))
        arg2 = float(input("Podaj argument 2: "))
        if op == "+":
            res = arg1 + arg2
            print("Wynik:", res)
            continue

        elif op == "-":
            res = arg1 - arg2
            print("Wynik:", res)
            continue

        elif op == "/":
            if arg2 != 0:
                res = arg1 / arg2
                print("Wynik:", res)
                continue
            else:
                print("Niepoprawne dane")
                continue

        elif op == "*":
            res = arg1 * arg2
            print("Wynik:", res)
            continue

        elif op == "**":
            res = arg1 ** arg2
            print("Wynik:", res)
            continue

        elif op == "root":
            if arg1 % 2 == 0 and arg2 < 0:
                print("Niepoprawne dane")
                continue
            else:
                res = arg2 ** (1 / arg1)
                print("Wynik:", res)
                continue

        elif op == "%":
            if arg2 != 0:
                res = arg1 % arg2
                print("Wynik:", res)
                continue
            else:
                print("Niepoprawne dane")
                continue

        elif op == "log":
            if arg1 > 1:
                res = math.log(arg2, arg1)
                print("Wynik:", res)
                continue
            else:
                print("Niepoprawne dane")
                continue
        else:
            print("Podaj poprawny operator")
            continue

