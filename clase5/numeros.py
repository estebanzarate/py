num = int(input("Ingresá un numero: "))
suma = 0

while num != 0:
    suma += num
    num = int(input("Ingresá un numero: "))
    if num == 0:
        print("La suma de los numeros es: ", suma)
