##Se ingresa por teclado las cantidades de galletitas, queso y dulce, necesarios para ahcer una torta
#Las cantidades se ingresan en kilos
#Cada torta insume:
#450 gramos de galles
#250 gramos de queso
#125 gramos de dulce
#¿Cuántas tortas se pueden hacer con la cant ingresada?
cgalle, cdulce, cqueso = 450,125,25

galle = int(input("Cantidad de galletitas "))
queso = int(input("Cantidad de queso "))
dulce = int(input("Cantidad de dulce "))

galle = galle*1000
queso = queso*1000
dulce = dulce*1000

#### // me da el cociente ENTERO -> 5//2 = 2
galle = galle//cgalle
queso = queso//cqueso
dulce = dulce//cdulce

if galle<queso and galle<dulce:
    print(galle, " Tortas sobre galle")
elif queso<galle and queso<dulce:
    print(queso, " Tortas sobre queso")
else:
    print(dulce, " Tortas sobre dulce")
