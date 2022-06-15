nombre = input('Ingresa el nombre de tu mascota: ')
edad = int(input('Ingresa la edad de tu mascota: '))
raza = input('Ingresa la raza de tu mascota: ')

mascota = {
    'Nombre': nombre,
    'Edad': edad,
    'Raza': raza
}

f = open('clase8/miMascota.txt', 'w')
f.write(mascota['Nombre'] + ',' +
        str(mascota['Edad']) + ',' + str(mascota['Raza']))
f.close()
