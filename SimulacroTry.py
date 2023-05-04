import random
"""def primos"""
def primos(nro):
    div,contdiv=1,0
    while div<=nro:
        if nro%div==0:
            contdiv=contdiv+1
        div=div+1
if contdiv<=2:
    print(nro,end=" ")
"""def raiz"""
def raiz(nro):
    cont=1
    while cont*cont<nro:
        cont=cont+1
    if cont*cont==nro:
        return 1
cprimos,mul2,oro5,esp7,raiz= 0,0,0,0,0
for i in range(80):
    palo=ramdom.randint(1,4)
    carta=random.randint(1,12)
    res1=primos(carta)
    if res1==1:
        cprimos=cprimos+1
        print(carta,end=" ")
    if carta%2==0:
        mul2=mul2+1
    if carta ==5 and palo==1:
        oro5=oro5+1
    if carta==7and palo==3:
        esp7=esp7+1
res2=raiz(carta)
if res2==1:
    raiz=raiz+1
print()
print("primos", cprimos)
print("eps 7", esp7)
print("5 oro", oro5/80/100)
print("con raiz", raiz)
print("mult2",raiz)
