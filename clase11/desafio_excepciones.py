from traceback import print_tb


def dividir(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'No se puede dividir por cero'


print(dividir(3, 1))
