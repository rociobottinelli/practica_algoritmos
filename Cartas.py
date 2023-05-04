#Generar dos numeros aleatorios, el primero entre 1 y 4. Siendo:
#1 - Copa
#2 - Basto
#3 - Oro
#4 - espada
#El segundo numero es el valor de la carta entre 1 y 12. Arrojar 80 cartas. Informar:
# Cuántas veces salió el 7 de espadas? El oro? Porcentaje de veces que salió el AS (1) de espada

import random
cant_as, cant_siete_esp, cant_oro = 0,0,0
for i in range(80):
    palo = random.randint(1,4)
    numero = random.randint(1,12)
    if palo == 3:
        cant_oro = cant_oro+1
    elif palo == 4 and numero == 1:
        cant_as= cant_as +1
    elif palo == 4 and numero == 7:
        cant_siete_esp = cant_siete_esp +1
print("Cantidad de siete de espada ", cant_siete_esp)
print("Cantidad de oro ", cant_oro)
promedio_as = cant_as * 100 /80
print("Promedio de AS ", promedio_as)

        
