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

# Clase 3

### Operadores relacionales

1. En una lista encontraremos diferentes operaciones relacionales, calcular mentalmente el resultado de cada expresión y almacenarlo en una nueva lista que contendrá únicamente valores lógicos True y False.
   expresiones = [
   False == True,
   10 >= 2*4,
   33/3 == 11,
   True > False,
   True*5 == 2.5*2
   ]

### Operadores lógicos

En una lista encontraremos diferentes operaciones lógicas. Calcular mentalmente el resultado de cada expresión y almacenarlo en una nueva lista la cual contendrá únicamente valores lógicos True y False.

expresiones = [
not False,
not 3 == 5,
33/3 == 11 and 5 > 2,
True or False,
True*5 == 2.5*2 or 123 >= 23,
12 > 7 and True < False
]

### Expresiones anidadas

A partir de dos variables llamadas NOMBRE y EDAD, debes crear una variable que almacene si se cumplen TODAS las siguientes condiciones, encadenando operadores lógicos en una sola línea:
NOMBRE sea diferente de cuatro asteriscos “\*\*\*\*”
EDAD sea mayor que 10 y a su vez menor que 18
Que la longitud de NOMBRE sea mayor o igual a 3 pero a la vez menor que 10
EDAD multiplicada por 4 sea mayor que 40
Desde un input conseguir las variables:
nombre = INPUT!!!
edad = INPUT!!!!

# Clase 4

### Mayoría de edad

1. Escribir un programa que le pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

-   Nota: Para preguntarle al usuario, recuerda usar input

### Marvel vs CapCom

Un curso se ha dividido en dos grupos: A y B de acuerdo al nombre y a una preferencia (Marvel o Capcom). El grupo A está formado por fans de Marvel con un nombre anterior a la M y los fans de Capcom con un nombre posterior a la N y el grupo B por el resto.

1. Escribir un programa que pregunte al usuario su nombre y preferencia, y muestre por pantalla el grupo que le corresponde.
   Ej:
   ¿Cómo te llamas? Alan
   ¿Cuál es tu preferencia (M o C)? C
   Tu grupo es B

-   Para preguntarle al usuario, recuerda usar input

# Clase 5

### Números

1. Escribir un programa que le pregunte al usuario números hasta que ingrese el 0, cuando lo haga mostrar por pantalla la suma de todos los números ingresados.

-   Nota: Para preguntarle al usuario, recuerda usar input

### Ejercicios varios

Haremos el siguiente listado de ejercicios:

1. Escribir un programa que enumere los países de la siguiente lista:-------3
   paises = ['Canada', 'USA', 'Mexico', 'Australia', Argentina, China, India]
2. Crear un bucle que sume los pares del 0 al 100-------------1
3. Imprimir por pantalla los números del 1 al 10 al revés-----------2
4. Pedirle a un usuario que ingrese un número, y devolver los dígitos totales del número
    - Por ejemplo, si el número es 75869, la salida debería ser 5.----------4
      Nota:
    - Para imprimir por pantalla al reves se debe usar el mayor número, luego el menor, y el paso sería con -1 range(mayor, menor, -1)

### Control de flujo

Desafío entregable 3 (Clase 5)
"Control de flujo"

1. Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:

-   Mostrar una suma de los dos números
-   Mostrar una resta de los dos números (el primero menos el segundo)
-   Mostrar una multiplicación de los dos números
-   Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
-   En caso de no introducir una opción válida, el programa informará de que no es correcta.

Respuesta

2. Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

3. Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:

🖐 Ayuda: Podes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números.

4. Escribí un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética: ♥♥♥

5. Escribí un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
   🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)

Respuesta
numeros = [1, 3, 6, 9]

6. Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

🖐 Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))

7. Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:

Respuesta
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

# Clase 6

### Desafío de sets

-   Programa las siguientes instrucciones de forma ordenada sobre la variable grupo:

2. Añade los usuarios: Ana, Ramón, Marta, Eric, David
3. Elimina los usuarios: Mario, Miguel, Esteban

grupo = {"Miguel", "Blanca", "Mario", "Andrés"}

### Desafío de sets

Programa las siguientes instrucciones de forma ordenada sobre la variable animales:

Inicialmente el diccionario es: animales = {"elefante": ""}

1. Añade al diccionario las claves perro, tigre y mono con sus respectivos valores “Bobby”, “Peepe” y “homero”
2. Modificá las claves elefante y delfin con los valores “Trompis”y “Manolo” respectivamente

# Clase 7

### Colecciones 1

1. Utilizando todo lo que sabes sobre cadenas, listas y sus métodos internos, transforma este texto:
   gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista

### Colecciones 2

A partir de una lista realizar las siguientes tareas sin modificar la lista original:

1. Borrar los elementos duplicados
2. Ordenar la lista de mayor a menor
3. Eliminar todos los números impares
   ( for ---- if (%2==1) ---- pop, remove )
4. Realizar una suma de todos los números que quedan
   (sum(lista))
5. Añadir como primer elemento de la lista la suma realizada insert(0, suma)
6. Devolver la lista modificada
7. Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

Nota: Recorda que para sumar todos los números de una lista puedes usar sum

# Clase 8

### Mi mascota

1. Crea un programa que pida por teclado (input) los datos de tu mascota y los mismos se guarden en un archivo que se llame miMascota.txt.

EXTRA: Hacerlo con un for o un while para no repetir tanto…!!!

### Curiosos por la información

1. Descargar y guardar en sus Drive algún dato en formato csv de las fuentes que les dimos, o de cualquier otra, leerlos y agruparlos por alguna de las columnas, como hicimos en el ejemplo agrupando por “sede”.

-   Datos ciudad de Buenos Aires: https://data.buenosaires.gob.ar/dataset/
-   Datos Nación: https://datos.gob.ar/

# Clase 9

### Par o impar

1. Realizar una función llamada par_o_impar:

-   Recibirá un número por parámetro
-   Imprimirá Par si el número es par
-   Imprimirá Impar si el número es impar
-   Si se ingresa algo que no sea número debe indicar que se ingrese un número. (Para los más audaces)

### Función año bisiesto

> > Consigna: Realizar una función llamada año_bisiesto:

-   Recibirá un año por parámetro
-   Imprimirá “El año año es bisiesto” si el año es bisiesto
-   Imprimirá “El año año no es bisiesto” si el año no es bisiesto
-   Si se ingresa algo que no sea número debe indicar que se ingrese un número.

    > > Información a tener en cuenta al realizar el entregable:

-   Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.
