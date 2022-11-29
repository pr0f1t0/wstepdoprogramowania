def wyświetl(**kwargs):
    for i in kwargs.keys():
        if "end" in kwargs:
            print(i, kwargs[i], end= kwargs.get("end"))
        else:
            print(i, kwargs[i])

wyświetl(a = 12, g = "B", end="/\n " )
