def sum_of_values(dict):
    sum = 0
    for i in dict.values():
        sum += i
    return sum

x = sum_of_values({'1': -1, '2': -2, '3': -3})
print(x)

