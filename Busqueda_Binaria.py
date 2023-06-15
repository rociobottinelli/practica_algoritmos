##Busqueda binaria

a=[1,2,3,5,8,15,20]

nro = 25
mini=0
pos=-1
maxi=len(a)-1

while mini<=maxi and pos == -1:
    med=(mini+maxi)//2
    if nro == a[med]:
        pos = med
    elif nro>a[med]:
        mini=med+1
    else:
        maxi=med-1
if pos != -1:
    print("Esta en la posicion ", pos)
else:
    print("No esta")
