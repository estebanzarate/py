# 1. Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
# num1 = int(input('Ingresa un número '))
# num2 = int(input('Ingresa otro número '))

# seleccion = int(input('¿Qué operación deseas realizar? 1, 2, 3, 4\n'))
# while seleccion != 4:
#     if seleccion != 1 or 2 or 3 or 4:
#         print('Ingresa una opción válida')
#     if seleccion == 1:
#         print('La suma de los números es', num1 + num2)
#     elif seleccion == 2:
#         print('La resta de los números es', num1 - num2)
#     elif seleccion == 3:
#         print('La multiplicación de los números es', num1 * num2)
#     elif seleccion == 4:
#         break
#     seleccion = int(input('¿Qué operación deseas realizar? 1, 2, 3, 4'))

# 2. Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.
# num = int(input(('Ingresa un número impar ')))
# while num % 2 == 0:
#     num = int(input(('Ingresa un número impar ')))

# 3. Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:
# suma = 0
# for i in range(0, 100):
#     if i % 2 != 0:
#         print(i)
#         suma += i
# print('La suma de los números impares es', suma)

# 4. Escribí un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:
# nums = []
# cantidad = int(input('¿Cuántos números querés introducir? '))
# for i in range(cantidad):
#     nums.append(int(input('Ingresa un número ')))
# media = sum(nums) / len(nums)
# print('La media de los números es', int(media))

# 5. Escribí un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
# Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista(devuelve True o False)

# 6. Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
# Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# list = []
# for i in range(0, 11):
#     list.append(i)
# print(list)
# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# list = []
# for i in range(-10, 1):
#     list.append(i)
# print(list)
# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# list = []
# for i in range(0, 21, 2):
#     list.append(i)
# print(list)
# Todos los números impares entre - 20 y 0 [-19, -17, -15, ..., -1]
# list = []
# for i in range(-20, 0):
#     if (i % 2) == 0:
#         continue
#     list.append(i)
# print(list)
# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
# list = []
# for i in range(0, 51):
#     if i % 5 == 0:
#         list.append(i)
# print(list)

# 7.Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:
# lista_1 = ["h", 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
# lista_2 = ["h", 'o', 'l', 'a', ' ', 'l', 'u', 'n', 'a']
# lista_3_copy = lista_1 + lista_2
# lista_3 = []

# for i in lista_3_copy:
#     if lista_3_copy.count(i) == 1:
#         lista_3.append(i)
# print(lista_3)
