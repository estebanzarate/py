nombre = input("Ingresá tu nombre: ")
preferencia = input("Cuál es tu preferencia (M o C)?")
if (preferencia == "M" and nombre < "M" or preferencia == "C" and nombre > "N"):
    print('Tu grupo es el A')
else:
    print('Tu grupo es el B')
