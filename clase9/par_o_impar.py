def par_o_impar(num):
    if type(num) != int:
        print('Ingresa un número')
    elif num % 2 == 0:
        print('Par')
    else:
        print('Impar')


par_o_impar(15)
