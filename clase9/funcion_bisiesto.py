def año_bisiesto(year):
    if type(year) != int:
        print('Ingresa un número')
    elif year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        print(f'El año {year} es bisiesto')
    else:
        print(f'El año {year} no es bisiesto')


año_bisiesto(2012)
