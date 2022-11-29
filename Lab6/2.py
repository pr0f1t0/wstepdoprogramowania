def oblicz(x,y):
    suma=x+y
    roznica=x-y
    return suma,roznica
    #return x+y,x-y

print(oblicz(10,5))
a,b=oblicz(10,5)
print(f'suma={a},roznica={b}')