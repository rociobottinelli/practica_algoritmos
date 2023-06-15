#1. Dado 0 y 1 generar la sucesión de Fibonacci hasta que , a partir de la posición 10, aparezca un nro con raiz cuadrada exacta. Informar cual es el nro.

#Rutina raiz
def raiz(a):
    cont=1
    while cont*cont<a:
        cont=cont+1
    if cont*cont == a:
        return 1

#Genero Fibonacci
fibo, i,signal = [0,1],2,0
while signal == 0:
    nro = fibo[i-2]+fibo[i-1]
    if i > 10:
        if raiz(nro) == 1:
            fibo.append(nro)
            signal = 1
        else:
            fibo.append(nro)
    else:
        fibo.append(nro)
    i = i+1
print("El valor ", nro, "tiene raiz exacta")
#Va a dar 144

#2. Completar una lista con valores entre 10 y 750 (cantidad = 30).
#Pasar a una segunda lista aquellos nros cuya suma de digitos sea impar.
#Ordenar esta segunda lista de forma sucedente. Ingresar un valor y buscarlo
#por búsqueda binaria. Informar en que posici+on se encuentra. 
#Obtener la suma de los dígitos con una función.
print("Ejercicio 2")
def suma(nro):
    sumDig=0
    while nro>0:
        dig=nro%10
        sumDig = sumDig +dig
        nro = nro // 10
    return sumDig
lista = []
impares = []
import random
for i in range(30):
    nro = random.randint(10,750)
    lista.append(nro)
    sumaNro = suma(nro)
    if sumaNro % 2 != 0:
        impares.append(nro)
for i in range(len(impares)-1):
    for j in range(i+1, len(impares)):
        if impares[i]>impares[j]:
            aux=impares[i]
            impares[i]=impares[j]
            impares[j]=aux
print(impares)
valor = int(input("Ingresar un valor: "))
mini = 0
pos = -1
maxi = len(impares)-1
while mini <= maxi and pos == -1:
    med = (mini + maxi) // 2
    if valor == impares[med]:
        pos=med
    elif valor > impares[med]:
        mini = med +1
    else:
        maxi = med -1
print("Impares:", impares)
print("Posición:", pos)
print("Suma de la posición:", suma(pos))
print("La posición es", pos)
