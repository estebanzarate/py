def f(*args):
    segundos = 0
    minutos = 0
    horas = 0
    if len(args) == 1:
        segundos = args[0]
        minutos = args[0] // 60
        horas = args[0] // 3600
        print('Segundos', segundos, 'Minutos', minutos, 'Horas', horas)
    elif len(args) == 3:
        segundos = (args[0] * 3600) + (args[1] * 60) + args[2]
        print(segundos, ' segundos')


f(120)
