"""
Un for bucle utiliza un iterador para recorrer una secuencia, por ejemplo, un rango de números,
los elementos de una lista, etc. En términos simples, el iterador es una variable que recorre la lista.

El iterador comienza desde el principio de la secuencia. En cada iteración, el iterador se actualiza al siguiente
valor de la secuencia.

En un forbucle, debemos definir tres cosas principales:

El nombre del iterador.
La secuencia a recorrer
El conjunto de operaciones a realizar.
El bucle siempre comienza con la forpalabra clave. El cuerpo del bucle tiene sangría hacia la derecha:

"""

print("* rango")

"""
En Python, la función incorporada range()se puede utilizar para crear una secuencia de números enteros. 
Esta secuencia se puede repetir a través de un bucle. Un rango se especifica en el siguiente formato:

range(start, end, step)

"""
print(type(range(1,100,5)))
print(list(range(1,100,5)))

print("* for")
for i in range(1, 9):  # A sequence from 1 to 10
    if i % 2 == 0:
        print(i, " is even")
    else:
        print(i, " is odd")

for i in range(1, 11, 3):  # A sequence from 1 to 10 with a step of 3
    print(i)

print("* Recorriendo una lista/cadena")

float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
print(float_list)

for i in range(0, len(float_list)):  # Iterator traverses to the last index of the list
    float_list[i] = float_list[i] * 2

print(float_list)

float_list_new = [1, 2, 3, 4, 4]

for float_new in float_list_new:  # Iterator traverses to the last index of the list
    print(float_new)

float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
count_greater = 0

for num in float_list:  # Iterator traverses to the last index of the list
    if num > 10:
        count_greater += 1

print(count_greater)