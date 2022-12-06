import numpy as np
macierz = np.random.randint(low=-10, high= 20, size=(5, 5))
print(macierz)
print(f"Wartość maksymalna: {macierz.max()}\nWatrość minimalna:{macierz.min()}")
print(f"Wartość maksymalna w wierszach: {macierz.max(axis=1)}, wartość maksymalna w kolumnach: {macierz.max(axis=0)} ")
print(f"Suma wierszów: {macierz.sum(axis=1)}, suma kolumn: {macierz.sum(axis=0)}")

