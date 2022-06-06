lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

# Añade a la LISTA1 el int 1234
lista1.append(1234)
print('Lista 1', lista1)
# y luego el string "Hola"
lista1.append('hola')
print('Lista 1', lista1)

# Añade a la LISTA2 el string "Adios"
lista2.append('Adios')
print('Lista 2', lista2)
# y luego el int 1234
lista2.append(1234)
print('Lista 2', lista2)

# Genera una LISTA3 con todos los elementos de la LISTA1 menos el último
lista1.pop()
lista3 = lista1
print('Lista 3', lista3)

# Genera una LISTA4 con todos los elementos de la LISTA2 menos el primero y el último
lista2.pop()
lista2[:1] = []
lista4 = lista2
print('Lista 4', lista4)

# Genera una LISTA5 con todos los elementos de la LISTA4 y LISTA3
lista5 = lista4 + lista3
print('Lista 5', lista5)