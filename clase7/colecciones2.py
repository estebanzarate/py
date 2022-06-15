# A partir de una lista realizar las siguientes tareas sin modificar la lista original:
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

# 1. Borrar los elementos duplicados
# for i in lista:
#    if lista.count(i) > 1:
#        lista.remove(i)
# print(lista)

# 2. Ordenar la lista de mayor a menor
# lista.sort(reverse=True)
# print(lista)

# 3. Eliminar todos los números impares
# (for ---- if ( % 2 == 1) - --- pop, remove)
for i in range(len(lista) - 1, -1, - 1):
    if lista[i] % 2 != 0:
        lista.remove(lista[i])

# 4. Realizar una suma de todos los números que quedan
# (sum(lista))
suma = sum(lista)

# 5. Añadir como primer elemento de la lista la suma realizada insert(0, suma)
lista.insert(0, suma)

# 6. Devolver la lista modificada
print(lista)

# 7. Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista
# Nota: Recorda que para sumar todos los números de una lista puedes usar sum
if sum(lista) - lista[0] == lista[0]:
    print('Concuerdan')
