import random as r
X = [r.randint(0, 10) for i in range(10)]
print(X)
X[0:3], X[-3:] = X[-3:], X[0:3]
print(X)
