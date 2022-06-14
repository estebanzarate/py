# Escribir un programa que enumere los países de la siguiente lista: -------3
paises = ['Canadá', 'USA', 'Mexico',
          'Australia', 'Argentina', 'China', 'India']

for inx, pais in enumerate(paises):
    inx += 1
    print(inx, pais)

# Crear un objeto que sume los pares del 0 a 100
suma = 0
for num in range(0, 100):
    if num % 2 == 0:
        suma += num

print('La suma de los números pares es:', suma)

# Imprimir por pantalla los números del 1 al 10 al revés
for num in range(10, 0, -1):
    print(num)

# Pedirle a un usuario que ingrese un número, y devolver los dígitos totales del número
numero = int(input('Ingresá un número: '))
print('El número ingresado tiene', len(str(numero)), 'dígitos')
	