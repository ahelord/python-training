"""
na función puede convertirse en argumento de otra función. Esto es útil en muchos casos.

Hagamos una calculator función que requiera la función add, subtract, multipl yo divide junto con dos números como argumentos.

"""

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function


result = calculator(multiply, 10, 20)
print(result)
print(calculator(add, 10, 20))

print("* usando lambdas")
"""
Para el calculatormétodo, necesitábamos escribir cuatro funciones adicionales que pudieran usarse como argumento. Esto puede resultar bastante complicado.

¿Por qué no pasamos simplemente una lambda como argumento? Las cuatro operaciones son bastante simples, por lo que pueden escribirse como lambdas.
"""

def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function


# 10 and 20 are the arguments.
result = calculator(lambda n1, n2: n1 * n2, 10, 20)
# The lambda multiplies them.
print(result)

print(calculator(lambda n1, n2: n1 + n2, 10, 20))

"""
Ésta es la belleza de las lambdas. Funcionan muy bien como argumentos para otras funciones.
"""

print("* function map")
"""
La función incorporada map()crea un objeto de mapa utilizando una lista existente y una función como parámetros. Este objeto se puede convertir en una lista usando la list()función.

La plantilla para map()es la siguiente:

map(function, list)

Se function aplicará, o se asignará , a todos los elementos del list.

A continuación, usaremos map()para duplicar los valores de una lista existente:

"""

num_list = [0, 1, 2, 3, 4, 5]

double_list = map(lambda n: n * 2, num_list)

print(list(double_list))


print("* filter")
"""
Otro ejemplo similar es la filter() función. Requiere una función y una lista.

filter() filtra elementos de una lista si los elementos satisfacen la condición especificada en la función de argumento.

Escribamos una filter() función que filtre todos los elementos que sean mayores que 10:
"""

numList = [30, 2, -15, 17, 9, 100]

greater_than_10 = list(filter(lambda n: n > 10, numList))
print(greater_than_10)

"""
La función devuelve un objeto de filtro que se puede convertir en una lista usando list().

al igual que map(), filter()devuelve un nuevo objeto sin cambiar la lista original.

A estas alturas, comprendemos mejor cómo las funciones pueden convertirse en argumentos y por qué las lambdas son útiles en esa situación.
"""