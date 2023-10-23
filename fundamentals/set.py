"""
Un conjunto es una colección desordenada de elementos de datos.

Los datos no están indexados, por lo que no podemos acceder a elementos usando índices o get().

Esta es quizás la estructura de datos más simple de Python. Podemos pensar en ello como una bolsa que contiene elementos aleatorios.

No se pueden agregar estructuras de datos mutables como listas o diccionarios a un conjunto. Sin embargo, agregar una tupla está perfectamente bien.

Uno podría preguntarse: "¿Por qué necesitaría un juego?"

Bueno, un conjunto es perfecto cuando simplemente necesitamos realizar un seguimiento de la existencia de elementos.
"""

print("* creando un conjunto")
random_set = {"Educative", 1408, 3.142,
              (True, False)}
print(random_set)
print(len(random_set))  # Length of the set

print("* constructor")
empty_set = set()
print(empty_set)

random_set = set({"Educative", 1408, 3.142, (True, False)})
print(random_set)

print("* agregar elementos")
"""
Para agregar un solo elemento, podemos usar el add()método. Para agregar varios elementos, tendríamos que usar update().

La entrada update()debe ser otro conjunto, lista, tupla o cadena.

Agreguemos elementos a un conjunto vacío:
"""

empty_set = set()
print(empty_set)

empty_set.add(1)
print(empty_set)

empty_set.update([1, 1, 2, 3, 4, 5, 6])
print(empty_set)

print("* remover elemento")
random_set = set({"Educative", 1408, 3.142, (True, False)})
print(random_set)

random_set.discard(1408)
print(random_set)

random_set.remove((True, False))
print(random_set)
"""
El remove()método genera un error si no se encuentra el elemento, a diferencia del discard()método.
"""

print("* iterando un conjunto")
"""
El forbucle se puede utilizar en estructuras de datos desordenadas como conjuntos. 
Sin embargo, no sabríamos el orden en el que se mueve el iterador, lo que significa que los elementos se seleccionarán al azar.
"""

odd_list = [1, 3, 5, 7]
unordered_set = {9, 10, 11, 12, 13, 14, 15, 16, 17}

print(unordered_set)

for num in unordered_set:
    if(not num % 2 == 0):
        odd_list.append(num)

print(odd_list)

print("* operaciones con conjuntos")
"""
Las personas familiarizadas con las matemáticas sabrán que los conjuntos tienen tres operaciones principales: unión , intersección y diferencia .
"""
print("* union")
set_A = {1, 2, 3, 4}
set_B = {'a', 'b', 'c', 'd'}

print(set_A | set_B)
print(set_A.union(set_B))
print(set_B.union(set_A))

print("* interseccion")
set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}

print(set_A & set_B)
print(set_A.intersection(set_B))
print(set_B.intersection(set_A))

print("* diferencia")
"""
En Python, la diferencia entre dos conjuntos se puede encontrar utilizando el -operador o el difference()método.

Tenga en cuenta que la operación de diferencia no es asociativa , es decir, las posiciones de los conjuntos importan.

set_A - set_Bdevuelve los elementos que sólo están presentes en set_A.

set_B - set_Aharía lo contrario.
"""

set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}


print(set_A - set_B)
print(set_A.difference(set_B))

print(set_B - set_A)
print(set_B.difference(set_A))

print("* frozenset")
"""
Es un tipo de dato exactamente igual que un set, con la diferencia de que es inmutable.
"""
fset = frozenset({"azul, amarillo, verde"})
print(fset)
