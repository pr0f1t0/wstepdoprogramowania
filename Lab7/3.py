import numpy as np
tablica = np.zeros((3,3))
"""tablica[1:, :2] = 1
print(tablica)"""
"""tablica[:, 1:] = 1
print(tablica)"""
"""tablica[:2, :] = 1
print(tablica)"""
"""tablica[:2, 0] = 1
print(tablica)"""
tablica[:2, [0, 2]] = 1
print(tablica)
