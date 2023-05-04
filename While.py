##WHILE

suma,contador=0,1
while contador <= 10:
    suma= suma + contador
    contador= contador + 1
    print("La suma es ", suma, end="") #Te lo junta todo
print("La suma total es ", suma)

##RANDOM
import random
print(random.randint(1,27))

#1. Generar 50 números correspondientes a los lados de un dado y mostrarlos.

import random
contador=0
while contador <= 50:
    print(random.randint(1,6),end=", ")
    contador=contador + 1
print("Fin")

##SUCESIÓN DE FIBONACCI -> Cada valor se genera por la suma de los dos anteriores, hasta el infinito.
# Ej: 0 1 1 2 3 5 8 13 etc

##NÚMEROS PRIMOS -> Números que sólo son divisibles por 1 y por sí mismos, dando resultado entero.
##¿Cómo lo sé? Divido con los numeros de atrás y sólo deben haber dos resto cero.

# WHILE por Evento.
suma=0
imp = int(input("First"))
while imp != -1:
    suma = suma + imp
    imp = int(input())
print("El total vendido fue ", suma)

##FOR -> necesito saber cuantas vueltas va a dar, si no sé no se puede usar,

for variable in range(0,19,2):
    print(variable)
#Printeavalores de 2 en 2, excluyendo el 19 porque es en cantidad y arranca en 0

# 1. Generar 500 valores entre 0 y 36. Informar cuantos valores saliendo de la segunda docena (entre 13 y 24)

import random
docena2 = 0
for i in range(500):
    numero= random.randint(0,36)
    if numero <= 36 and numero >= 13:
        docena2=docena2+1
print("Salieron ", docena2, " de la segunda docena")


