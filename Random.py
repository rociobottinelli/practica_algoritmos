##Generar 50 numeros correspondientes a los lados de un dado y mostrarlos
##Informar cuantos valores entre 2 y 4 inclusive.

import random
cont, cant1y2 = 0,0
while cont < 50:
    nro = random.randint(1,6)
    print(nro, end=" ")
    if nro>=2 and nro <=4:
        cant1y2 = cant1y2 + 1
    cont = cont + 1
print()
print("Salieron ",cant1y2, " numeros entre 2 y 4")
