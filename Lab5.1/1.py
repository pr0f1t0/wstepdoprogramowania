values = [10, 20, 30]
keys = ["ten", "twenty", "thirty"]
d = dict(zip(keys, values))
d1 = {}
for i in range(len(values)):
    d1[keys[i]]= [values[i]]
print(d1)

d2 = {keys[i]: values[i] for i in range(len(values))}
print(d2)
print(d2)
