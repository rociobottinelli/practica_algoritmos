TEORÍA
Listas
a = [5,2,1]
len(a) -> 3
print(a[2]) -> 1
a.append(valor)

¿Como se recorren? Con un for o un while

ORDENAR LISTAS
* De menor a mayor

a=[5,1,2,8,3]

if a[0] > a[1]:
    aux=a[0]
    a[0]=a[1]

Eso es basicamente lo que hace en cada iteración

1. Un puntero que apunte al primer valor
2. Uno que apunte al segundo
3. ¿El primer valor es mayor al segundo -> Si es mayor lo doy vuelta
Mando a uno de los dos a una var auxiliar para poder hacer el cambio

En la primera barrida total logro que el valor máximo llegue al final.

BURBUJEO: ubica al mayor

for j in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            aux = a[i]
            a[i]=a[i+1]
            a[i+1]=aux
print(a)

DESCENDENTE -> MAYOR A MENOR (Invierto el símbolo)
ASCENDENTE -> MENOR A MAYOR


DE SELECCION -> UBICA AL MENOR
def selection_sort(lista):
    n = len(lista)
    
    for i in range(n - 1):
        min_index = i
        
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
                
        lista[i], lista[min_index] = lista[min_index], lista[i]

1. La función selection_sort toma una lista como parámetro.
2. Se obtiene la longitud de la lista y se almacena en la variable n.
3. El primer bucle for itera desde 0 hasta n - 1. Esto se debe a que después de cada iteración del bucle exterior,
el elemento más pequeño se coloca en su posición final, por lo que no es necesario volver a considerarlo en iteraciones posteriores.
4. Se inicializa la variable min_index con el valor de i, que representa el índice del elemento actual en cada iteración del bucle exterior.
5. El segundo bucle for itera desde i + 1 hasta n. Esto se debe a que después de cada iteración del bucle interior,
se busca el elemento más pequeño en la parte no ordenada de la lista.
6. Dentro del bucle, se compara si el elemento actual (lista[j]) es menor que el elemento mínimo actual (lista[min_index]).
Si es así, se actualiza min_index con el valor de j, que representa el índice del nuevo elemento mínimo encontrado.
7. Una vez que se completa el bucle interior, se intercambian los elementos en las posiciones i y min_index utilizando una asignación paralela de Python (lista[i], lista[min_index] = lista[min_index], lista[i]).
8. Después de que el bucle exterior se completa, la lista está ordenada de forma ascendente.

/Clase/


for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            aux=a[i]
            a[i]=a[j]
            a[j]=aux
            




















