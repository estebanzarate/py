# Clase 1

### Desafío números - Nota final

1. Crear un programa para calcular la nota final de un estudiante en base a dos exámenes, los exámenes cuentan con un porcentaje distinto de la nota final

    - nota_1 cuenta como el 40% de la nota final
    - nota_2 cuenta como el 60% de la nota final

### Desafío string - Reordenación

1. Dadas cuatro variables con diferentes textos (de forma individual), genera una nueva variable con el siguiente contenido:
    - Objetivo: “Python es un lenguaje de programación moderno”
2. Partiendo de:
    - cadena_1 = “moderno”
    - cadena_2 = “Python”
    - cadena_3 = “es un lenguaje”
    - cadena_4 = “de programación”

### Desafío slicing - Formatear

Se tiene una cadena de texto, pero al revés. Al parecer contiene el nombre de un alumno, la nota de un exámen y la materia.
De forma individual, realiza lo siguiente:

1. Dar vuelta la cadena y asignarla a una variable llamada cadena_volteada. Para devolver una cadena dada vuelta se usa el tercer índice negativo con slicing: cadena[::-1].
2. Extraer nombre y apellido, almacenarlo en una variable llamada nombre_alumno
   Extraer la nota y almacenarla en una variable llamada nota.
3. Extraer la materia y almacenarla en una variable llamada materia.
4. Mostrar por pantalla la siguiente estructura:
    - NOMBRE APELLIDO ha sacado un NOTA en MATERIA
      Formateando las anteriores variables en una variable llamada cadena_formateada
      cadena = “acitametaM ,5.8 ,otipeP ordeP”
      Para formatear ¡recuerda concatenar!

### Mi primer programa en Python

> > Consigna: Crear un programa para calcular la nota final del estudiante en base a dos exámenes, los exámenes cuentan con un porcentaje distinto de la nota final

-   nota_1 cuenta como el 40% de la nota final
-   nota_2 cuenta como el 60% de la nota final

> > Aspectos a incluir en el entregable:

-   Tener en cuenta los temas vistos en la clase 1: números, print, input, variables, operaciones matemáticas, cadena de texto.

    > > Aspectos a tener en cuenta:

-   Los datos deben guardarse en variables y deben ser dinámicos por medio de input.

# Clase 2

### Desafío de listas

-   Dadas dos listas LISTA1 y LISTA2 debes realizar las siguientes tareas:

1. Añade a la LISTA1 el int 1234 y luego el string “Hola”
2. Añade a la LISTA2 el string “Adios” y luego el int 1234
3. Genera una LISTA3 con todos los elementos de la LISTA1 menos el último
4. Genera una LISTA4 con todos los elementos de la LISTA2 menos el primero y el último
5. Genera una LISTA5 con los elementos de la LISTA4 y de la LISTA3

-   lista1 = [1, 12, 123]
-   lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

### Desafío de tuplas

1. A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada, lo siguiente:
    - El último ítem de tupla
    - El número de ítems de tupla
    - La posición donde se encuentra el ítem 87 de tupla
    - Una lista con los últimos tres ítems de tupla
    - Un ítem que haya en la posición 8 de tupla
    - El número de veces que el ítem 7 aparece en tupla

-   Copia esta tupla para iniciar el ejercicio:
    tupla = (5, 12, 7, 37, 8, 86, 19, 7, -783, 87, 188, 7, 9, 12, 7, 3982)

### Prácticas iniciales

> > Consigna:

1. Identifica el tipo de dato (int, float, string, list o touple) de los siguientes valores literales:

Dato
Tipo de datos
"Hola Mundo" ♥♥♥ STRING

[1, 10, 100] ♥♥♥ LIST

-25 ♥♥♥ INT

(1, 2, 3, 4, 5) ♥♥♥ TUPLE

(8, 100, -12) ♥♥♥ TUPLE

1.167 ♥♥♥ FLOAT

["Hola", "Mundo"] ♥♥♥ LIST

' ' ♥♥♥ STRING

(1, -5, "Hola!") ♥♥♥ TUPLE

2. Determina mentalmente (sin programar) el resultado que aparecerá por pantalla a partir de las siguientes variables:

a = 10
b = -5
c = "Hola"
d = [1, 2, 3]
e= (4,5,6)

Ejecutar
Resultado
print(a \* 5) ♥♥♥ 10

print(a - b) ♥♥♥ 15

print(c + "Mundo") ♥♥♥ "HolaMundo"

print(c \* 2) ♥♥♥ "HolaHola"

print(c[-1]) ♥♥♥ "a"

print(c[1:]) ♥♥♥ "ola"

print(d + d) ♥♥♥ [1, 2, 3, 1, 2, 3]

print(e[1]) ♥♥♥ 5

print(e+(7,8,9)) ♥♥♥ (4,5,6,7,8,9)

3. El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de identificar el problema y solucionarlo?

numero_1 = 9
numero_2 = 3
numero_3 = 6
​
media = numero_1 + numero_2 + numero_3 / 3
print("La nota media es", media)
La nota media es 14.0

Respuesta
♥♥♥ Primero divide numero_3 entre 3 y luego suma numero_1 y numero_2

4. A partir del ejercicio anterior, desarrolla un programa para calcular la nota final. Para ello vamos a suponer que cada número es una nota y que queremos obtener la nota media. Cada nota tiene un valor porcentual:

La primera nota vale un 15% del total
La segunda nota vale un 35% del total
La tercera nota vale un 50% del total

Ejemplos:
nota_1 = 10
nota_2 = 7
nota_3 = 4

Respuesta
media = (nota*1 * .15 + nota*2 * .35 + nota_3 \* .5) / 100

5. La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

🖐 Ayuda: La función llamada sum(lista) devuelve una suma de todos los elementos de la lista

Partirás de:
matriz = [
[1, 5, 1],
[2, 1, 2],
[3, 0, 1],
[1, 4, 4]
]

Debes llegar a:

matriz = [
[1, 5, 1, 7],
[2, 1, 2, 5],
[3, 0, 1, 4],
[1, 4, 4, 9]
]

Respuesta

♥♥♥ matriz = [
[1, 5, 1, sum(matriz[0])],
[2, 1, 2, sum(matriz[1]],
[3, 0, 1, sum(matriz[2]],
[1, 4, 4, sum(matriz[3]]
]
