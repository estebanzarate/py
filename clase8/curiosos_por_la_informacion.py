import pandas as pd

datosNacion = pd.read_csv('clase8/data.csv')

print(datosNacion.head(4))
print(datosNacion.tail(6))
print(datosNacion.sample(2))

print(datosNacion['FECHA'])
