import numpy as np
wagi_l = [2**i for i in range(7, -1, -1)]
wagi = np.array(wagi_l)
liczba_bin = np.random.randint(low=0, high=2, size=8)
il = liczba_bin * wagi
rez = 0
for i in il:
    rez += i
print(rez)




