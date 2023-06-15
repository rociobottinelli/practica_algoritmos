a=[23,67,2,89,11,9,3,57,1]

##Burbujeo -> ubica al mayor
#De menor a mayor
for j in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            aux = a[i]
            a[i]=a[i+1]
            a[i+1]=aux
print(a)

##Burbujeo
#De mayor a menor
for j in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            aux = a[i]
            a[i]=a[i+1]
            a[i+1]=aux
print(a)

##De seleccion -> ubica al menor
#De mayor a menor
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            aux=a[i]
            a[i]=a[j]
            a[j]=aux

print(a)

#De menor a mayor
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] < a[j]:
            aux=a[i]
            a[i]=a[j]
            a[j]=aux

print(a)
