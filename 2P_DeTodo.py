##PRACTICA PRE PARCIAL
#EJERCICIO 3
#Cargar una lista con 20 valores que tengan raíz cuadrada exacta, comprendidos entre 2 y 800, y que no se repitan
#Una vez cargada, pasar a otra lista, aquellos valores cuya suma de sus digitos sea par, por ejemplo: 400 (no eliminarlo de la primera lista)
#Ordenar la segunda lista por Selección, de mayor a menor, y mostrarla con los valores separados por 3 espacios
import random
def busqueda(valor, lista):
    for j in range(len(a) - 1):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                aux = a[i]
                a[i] = a[i + 1]
                a[i + 1] = aux
    
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

#def ordenar(a):
 #   for j in range(len(a) - 1):
  #      for i in range(len(a) - 1):
   #         if a[i] > a[i + 1]:
    #            aux = a[i]
     #           a[i] = a[i + 1]
      #          a[i + 1] = aux
    
    return a
def raizCuadrada(nro):
    cont=1
    while cont * cont < nro:
        cont = cont +1
    if cont * cont == nro:
        return 1

def suma(nro):
    sumadig=0
    while nro !=0:
        dig = nro % 10
        sumadig = sumadig + dig
        nro = nro // 10
    if sumadig % 2 == 0:
        return 1

a = []
b = []

while len(a) < 20:
    nro = random. randint(2,800)
    repeticion = busqueda(nro,a)
    raiz = raizCuadrada(nro)
    if repeticion == -1 and raiz == 1:
        a.append(nro)
        sumaPar = suma(nro)
        if sumaPar == 1:
            b.append(nro)
print(a)
print(b)
##DE SELECCION MAYOR A MENOR
for i in range(len(b)-1):
    for j in range(i+1, len(b)):
        if b[i] < b[j]:
            aux=b[i]
            b[i]=b[j]
            b[j]=aux

for i in range (len(b)):
    print(b[i],end="   ")
