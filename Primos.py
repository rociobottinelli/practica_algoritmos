## Encontrar cantidad de numeros primos en documentos
def primo(numero):
    divisor,contador=1,0
    while divisor < numero:
        if numero % divisor == 0:
            contador = contador + 1
        divisor = divisor + 1
    if contador <= 2:
        return 1

doc = int(input("Ingresar su DNI "))
cant_primos = 0
while doc != 0:
    digito = doc%10 #asi obtengo el ultimo
    res = primo(digito)
    if res == 1:
        cant_primos = cant_primos + 1

    doc = doc // 10 # y aca se lo saco
print("Cantidad de numeros primos en el documento ", cant_primos)
