##Practica pre-parcial
#Tips:
# 1. No se sale de forma forzada de un for
# 2. Validar en NEGATIVO, o sea vigilar que no estoy donde no debo estar.
# 3. Para usar búsqueda binaria debe estar ordenada de menor a mayor.

#Ejercicio 1
#Desarrolle un programa para que, ingresando un número entero, positivo y menor que 100, verificar esto,
#pueda informar si el valor ingresado es un número abundante, deficiente o perfecto 
#Considerar que si el número ingresado no es menor a 100, deberá solicitarlo nuevamente.  

res = int(input("Ingresar un número: "))
##Esto es validar en negativo
while res < 0 or res > 100:
    res = int(input("Reingrese: "))


#Defino funciones
def tipoNumero(nro):
    sumadiv = 0
    for i in range(1,nro):
        if nro%i == 0:
            sumadiv = sumadiv + i
    if sumadiv > nro:
        return 1
    elif sumadiv < nro:
        return 0
    else:
        return 5
sumDivisores = (tipoNumero(res))
if sumDivisores == 1:
    print("Es abundante")
elif sumDivisores == 0:
    print("Es deficiente")
else:
    print("Es perfecto")


