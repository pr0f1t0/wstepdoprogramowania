def znaki(string):
    słownik = {}
    for i in string:
        słownik[i] = słownik.get(i, 0) + 1
        """if i in słownik:
            słownik[i] += 1
        else:
            słownik[i] = 1"""
    return słownik

res = znaki("znaki napisu")
for i in sorted(res):
    print(f"{i}: {res[i]}")