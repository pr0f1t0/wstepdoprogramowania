values = ['thirty', 'fourty', 'fifty']
keys = [30, 40 ,50]
d = dict(zip(keys, values))
d1 = dict(thirty = 30, fourty = 40, fifty = 50) #metoda słów kluczowych
d2 = {}
d2 = d.copy()
d2.update(d1)
print(d2)
