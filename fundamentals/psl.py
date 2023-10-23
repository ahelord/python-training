"""
La biblioteca estándar de Python, PSL, es una colección de módulos predefinidos o conjuntos de métodos que nos ayudan a realizar determinadas tareas en Python.

La biblioteca contiene muchas utilidades útiles que nos ahorran mucho tiempo.
 Hay diferentes tipos de funciones matemáticas complejas, tipos de datos de alto nivel, herramientas de programación de redes, ¡y esto es sólo la punta del iceberg!

Generalmente, un módulo contiene funciones relacionadas con un aspecto particular de la programación.
 Esto facilita las cosas porque sabemos qué parte de nuestro programa requiere qué módulo.

En Python, podemos crear nuestros propios módulos, pero esa es una historia para otro momento. Nos centraremos en lo que Python nos ofrece listo para usar.
"""
print("* importar un modulo")
"""
Para utilizar los métodos de un módulo, debemos importar el módulo a nuestro código. Esto se puede hacer usando la importpalabra clave.

Importemos el datetimemódulo que contiene varios métodos relacionados con la fecha y hora actuales. Como siempre, se puede acceder a estos métodos utilizando el .operador:
"""
# Importing modules at the beginning of the program is a good practice

import datetime

date_today = datetime.date.today()  # Current date
print(date_today)

time_today = datetime.datetime.now()
print(time_today.strftime("%H:%M:%S"))  # Current time

"""
En el código anterior, datetime.datey datetime.datetimeson clases en el datetimemódulo. Cada clase contiene sus propios métodos.
Si solo queremos una clase particular de un módulo, podemos usar la frompalabra clave en el siguiente formato:

from module import class
"""


from datetime import date

# Now we only have the methods of the date class
date_today = date.today()  # Current date
print(date_today)

# These won't work
# time_today = datetime.datetime.now()
# print (time_today.strftime("%H:%M:%S"))# Current time

"""
También podemos dar nuestros propios nombres a los módulos que importamos usando la aspalabra clave. 
Cambiémosle datetime el nombre dt y usémoslo en el programa:
"""
import datetime as dt

date_today = dt.date.today()  # Current date
print(date_today)

time_today = dt.datetime.now()
print(time_today.strftime("%H:%M:%S"))  # Current time

print("* modulo math")
import math

fact_of_5 = math.factorial(5)  # The factorial of 5
print(fact_of_5)

gcd = math.gcd(300, 90)  # Greatest common denominator
print(gcd)

log100 = (math.log(10, 100))  # Logarithm of 10 to the base of 100
print(log100)

print("* modulo heapq")

"""
El heapq módulo nos permite crear la estructura de datos del montón .
 Un montón es un árbol binario que siempre almacena un valor especial en la parte superior (raíz). 
 Un minheap almacena el valor más pequeño en la parte superior y un maxheap almacena el valor más grande en la parte superior.
 
 El popmétodo devuelve el valor en la parte superior del montón.

Python heap qcrea un minheap de forma predeterminada.
"""
import heapq #arbol binario

heap = []  # Empty heap

# Inserting elements in the heap
heapq.heappush(heap, 10)
heapq.heappush(heap, 70)
heapq.heappush(heap, 5)
heapq.heappush(heap, 35)
heapq.heappush(heap, 50)

# Popping the smallest value
minimum = heapq.heappop(heap)
print(heap)
print(minimum)

print("* random")
import random

rand_num = random.random()
print(rand_num)

rand_num_in_range = random.uniform(30, 50)  # A random number between 30 and 50
print(rand_num_in_range)

str_list = ['a', 'b', 'c', 'd', 'e']
random.shuffle(str_list)  # Randomly shuffle a list
print(str_list)
