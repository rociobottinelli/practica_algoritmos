##Ingresar tres valores correspondientes a la longitud de los lados de un triángulo
#Informar:
    #A. Si los valores ingresados forman un triángulo
    #B. Si se forma un triángulo, qué triángulo es?
ladoA = int(input("Ingrese la longitud del lado A: "))
ladoB = int(input("Ingrese la longitud del lado B: "))
ladoC = int(input("Ingrese la longitud del lado C: "))
##Desigualdad triangular: la suma de dos lados debe ser mayor al tercero para que pueda ser un triángulo

if ladoA + ladoC <= ladoB or ladoC + ladoB <= ladoA or ladoA + ladoB <= ladoC:
    print("No es un triángulo")
elif ladoA == ladoB == ladoC:
    print("El triágulo es equilátero")
elif ladoA == ladoB or ladoB == ladoC or ladoC == ladoA:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")
