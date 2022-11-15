il = int(input("Podaj ilość zwierząt: "))
zwierzęta = [input("Nazwy zwierząt: ") for i in range(il)]
zwierzęta.sort()
print(zwierzęta)
print(zwierzęta[0], zwierzęta[-3:])
print(len(zwierzęta))


