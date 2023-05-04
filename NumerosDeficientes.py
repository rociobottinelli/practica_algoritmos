##Generar 50 valores entre 20 y 200
#Informar cuantos valores deificentes fueron generados
#Numero deficiente: (misma rutina que numero primo) es el
#numero cuta suma de dividores sin el propio numero es menor al numero
#Acordate que es DIVISOR SI SU RESTO DA 0
import random
cant_deficiente = 0
for i in range(50):
    numero = random.randint(20,200)
    divisor, suma_divisor = 1,0
    while divisor < numero:
        if numero % divisor == 0:
            suma_divisor = suma_divisor + divisor
        divisor = divisor + 1
    if numero > suma_divisor:
        cant_deficiente = cant_deficiente+1
print("La cantidad de deficientes es: ", cant_deficiente)
