nombre = input("Ingresá tu nombre: ")
edad = input("Ingresá tu edad: ")

almacenar = (nombre != "****") and (len(nombre) >= 3) and (len(nombre)
                                                           < 10) and (edad > 10) and (edad < 18) and (edad * 4 > 40)
print(almacenar)
