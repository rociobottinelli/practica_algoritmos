##SIMULACRO DE PARCIAL
import random

#FUNCIONES

def primos(nro):
    div, contdiv = 1, 0 # contdiv es la cantidad de divisores que tiene el numero, debe tener solo 2 o menos para ser primo
    while div <= nro:
        if nro % div == 0:
            contdiv = contdiv + 1
        div = div + 1
    if contdiv <= 2:
        return 1  # el return me saca de la funcion, asi que si por ej quiero poner un print debe ir antes
    else:
        return 0

    
def raiz(nro): #tiene raiz cuadrada entera?
    cont = 1
    while cont * cont < nro:
        cont = cont+1
    if cont * cont == nro:
        return 1


#Version pro
def raizPRO(nro): #tiene raiz cuadrada entera?
    cont = 1
    while nro>0:
        cont = cont+1
        nro = nro-cont
        cont = cont-2
        raices = raices + 1
    if nro == 0:
        return 1, raices  ## Retorno doble

##Ahora empieza el ciclo
cant_primos, mul2, oro5, esp7, cant_raices = 0, 0, 0, 0, 0

for i in range(80):   #genero los aleatorios
    palo = random.randint(1,4)
    carta = random.randint(1,12)
    res1 = primos(carta)
    if res1 == 1:
        cant_primos = cant_primos +1
        print(carta, end=" ")
    if carta % 2 == 0:   # modulo --> resto
        mul2 = mul2 + 1
    if carta == 5 and palo == 1:
        oro5 = oro5 + 1
    if carta == 7 and palo == 3:
        esp7 = esp7+1
res2 = raiz(carta)
if res2 == 1:
    cant_raices = cant_raices+1

        
print()
print("Primos: ", cant_primos)
print("Espada 7: ", esp7 )
print("Oro 5: %", oro5 / 80 * 100)
print("Con raiz: ", cant_raices)
print("Multiplo 2: ", mul2)
