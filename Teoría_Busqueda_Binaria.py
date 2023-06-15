TEORIA BUSQUEDA BINARIA
La búsqueda binaria es un algoritmo eficiente utilizado para buscar un elemento específico en una lista ordenada.
Funciona dividiendo repetidamente a la mitad la lista de búsqueda y comparando el elemento objetivo con el elemento central. Esto se hace hasta que se encuentre el elemento deseado o hasta que se reduzca el rango de búsqueda a cero.

Aquí tienes un ejemplo de cómo implementar la búsqueda binaria en Python:

```python
def binary_search(lista, elemento):
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        valor_medio = lista[medio]
        
        if valor_medio == elemento:
            return medio
        elif valor_medio < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    return -1
```

Explicación paso a paso:

1. La función `binary_search` toma dos parámetros: la lista en la que se realizará la búsqueda y el elemento que se desea encontrar.
2. Se inicializan dos variables `inicio` y `fin`. `inicio` representa el índice del primer elemento en el rango de búsqueda, y `fin` representa el índice del último elemento en el rango de búsqueda.
3. Se inicia un bucle `while` que se ejecuta mientras `inicio` sea menor o igual que `fin`. Esto indica que aún hay elementos en el rango de búsqueda.
4. Dentro del bucle, se calcula el índice del elemento central utilizando el promedio de `inicio` y `fin`. Esto se hace mediante la expresión `(inicio + fin) // 2`.
El uso del operador de división entera `//` asegura que obtengamos un número entero.
5. Se obtiene el valor del elemento central utilizando `lista[medio]` y se almacena en la variable `valor_medio`.
6. Se comparan `valor_medio` con el elemento objetivo. Si son iguales, significa que se ha encontrado el elemento y se devuelve el índice `medio`.
7. Si `valor_medio` es menor que el elemento objetivo, se actualiza `inicio` para que el rango de búsqueda se desplace hacia la mitad derecha de la lista.
8. Si `valor_medio` es mayor que el elemento objetivo, se actualiza `fin` para que el rango de búsqueda se desplace hacia la mitad izquierda de la lista.
9. Si el bucle termina sin encontrar el elemento objetivo, se devuelve `-1` para indicar que el elemento no está presente en la lista.

Aquí tienes un ejemplo de cómo usar la función `binary_search`:

```python
nums = [1, 2, 5, 8, 12]
elemento = 5

resultado = binary_search(nums, elemento)
if resultado != -1:
    print("El elemento", elemento, "se encuentra en el índice", resultado)
else:
    print("El elemento", elemento, "no se encuentra en la lista.")
```

La salida será:

```
El elemento 5 se encuentra en el índice 2
```

Si el elemento objetivo no está presente en la lista, se mostrará el mensaje "El elemento [elemento] no se encuentra en la lista.".

La búsqueda binaria tiene una complejidad de tiempo de O(log n), lo que la hace muy eficiente en comparación con otros métodos de búsqueda lineal para grandes conjuntos de
