####CONDICIONAL IF
## A. Ingresar un numero, informar si el mismo es + o - a 5
a = int(input("Ingrese el número "))
if a > 5:
    print("Es mayor")
else:
    print("No es mayor")
print("Fin")

# B. Ahora si es mayor, menor o igual
a = int(input("Ingrese el número "))
if a > 5:
    print("Es mayor")
else:
    if a == 5:
        print("Es igual")
    else:
        print("No es mayor")
print("Fin")

# C. Ingresar dos numeros que son notas de parcial 1 y 2. Informar:
    #1. Si recursa con promedio - a 4
    #2. Si rinde final con promedio + o == a 4 y menor a 7
    #3. Si promociona con promedio + o = a 7
nota1 = int(input("Ingrese nota primer parcial "))
nota2 = int(input("Ingrese nota segundo parcial "))
promedio = (nota1 + nota2)/2

if promedio >= 7:
    print("Promocionó")
if promedio == 3:
        print("Jajajaj ES 3")
else:
    if promedio >= 4:
        print("Rinde final")
    if promedio == 2:
        print("Jajajaj ES 2")
    else:
        print("Recursa")

#D. Ingresar 3 numero: A B y C. Mostrar suma B+C si A es par. Contrario, mostrar el producto

A = int(input("Ingrese el numero A "))
B = int(input("Ingrese el numero B "))
C = int(input("Ingrese el numero C "))

if A%2 == 0:
    print(B+C)
else:
    print(B*C)
print("Fin")
