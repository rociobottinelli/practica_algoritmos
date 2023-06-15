#PRACTICA PRE PARCIAL
#EJERCICIO 2
#Cargar una lista de 50 valores generados de forma aleatoria
#con valores entre 10 y 100, sin valores repetidos.
#Utilizar una función para determinar si está repetido 
#Mostrar la lista desordenada 
#Un vez cargado, ordenarlo por el método que guste (sort NO puede usar) 
#Mostrar la lista, ordenada 
#Ingresar un valor por teclado y buscarlo por búsqueda binaria. 
#Informar en que posición está o si no está
import random

def busqueda(valor, lista):
    mini = 0
    pos = -1
    maxi = len(lista) - 1
    
    while mini <= maxi and pos == -1:
        med = (mini + maxi) // 2
        
        if valor == lista[med]:
            pos = med
        elif valor > lista[med]:
            mini = med + 1
        else:
            maxi = med - 1
    
    if pos != -1:
        return pos
    else:
        return -1

def ordenar(a):
    for j in range(len(a) - 1):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                aux = a[i]
                a[i] = a[i + 1]
                a[i + 1] = aux
    
    return a

a = []
while len(a) < 50:
    nro = random.randint(10, 100)
    
    if len(a) == 0:
        a.append(nro)
    else:
        a = ordenar(a)
        estaRepetido = busqueda(nro, a)
        
        if estaRepetido == -1:
            a.append(nro)

print(a)

a = ordenar(a)
print(a)

valorBinario = int(input("Ingrese el valor a buscar: "))
res = busqueda(valorBinario, a)

if res == -1:
    print("El número no se encuentra en la lista.")
else:
    print("El número está en la posición", res)



