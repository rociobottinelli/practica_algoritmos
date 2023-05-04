##SUCESIÓN DE FIBONACCI-> La suma de los dos anteriores.
#Generar la sucesión hasta la posicion 15, partiendo de a=1 y b=1
#Arranco en contador con 2 porque los dos primeros son iniciales 1 y 1

a,b,c,cont = 1,1,0,2
while cont <= 15:
    c=a+b
    print(c, end=" ")
    a=b
    b=c
    cont= cont+1
