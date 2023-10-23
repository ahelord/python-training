"""
El principio de conversión entre estructuras de datos integradas en Python es similar al de los tipos de datos primitivos de Python.

Conversión explícita
La plantilla para convertir explícitamente de una estructura de datos a otra es la siguiente:

destination_structure_name(source_structure_object)

destination_structure_name es el nombre de la estructura de datos a la que queremos convertir.

source_structure_object es el objeto que queremos convertir.

"""
print("* convertir a lista")
"""
Podemos convertir una tupla, un conjunto o un diccionario en una lista usando el list()constructor. 
En el caso de un diccionario, sólo las claves se convertirán en una lista.
"""
star_wars_tup = ("Anakin", "Darth Vader", 1000)
print(star_wars_tup)
star_wars_set = {"Anakin", "Darth Vader", 1000}
print(star_wars_set)
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

star_wars_list = list(star_wars_tup)  # Converting from tuple
print(star_wars_list)

star_wars_list = list(star_wars_set)  # Converting from set
print(star_wars_list)

star_wars_list = list(star_wars_dict)  # Converting from dictionary
print(star_wars_list)

"""
También podemos usar el dict.items() método de un diccionario para convertirlo en un iterable de (key, value) tuplas. 
Esto se puede convertir en una lista de tuplas usando list():
"""
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

star_wars_list = list(star_wars_dict.items())
print(star_wars_list)

print("* conviertiendo a una tupla")
"""
Cualquier estructura de datos se puede convertir en una tupla utilizando el tuple() constructor. 
En el caso de un diccionario, sólo las claves se convertirán en tupla:
"""


star_wars_list = ["Anakin", "Darth Vader", 1000]
print(star_wars_list)
star_wars_set = {"Anakin", "Darth Vader", 1000}
print(star_wars_set)
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

star_wars_tup = tuple(star_wars_list)  # Converting from list
print(star_wars_tup)

star_wars_tup = tuple(star_wars_set)  # Converting from set
print(star_wars_tup)

star_wars_tup = tuple(star_wars_dict)  # Converting from dictionary
print(star_wars_tup)

print("* conviertiendo en conjunto")
"""
El set()constructor se puede utilizar para crear un conjunto a partir de cualquier otra estructura de datos.
En el caso de un diccionario, sólo las claves se convertirán en un conjunto:
"""
star_wars_list = ["Anakin", "Darth Vader", 1000]
print(star_wars_list)
star_wars_tup = ("Anakin", "Darth Vader", 1000)
print(star_wars_tup)
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

star_wars_set = set(star_wars_list)  # Converting from list
print(star_wars_set)

star_wars_set = set(star_wars_tup)  # Converting from tuple
print(star_wars_set)

star_wars_set = set(star_wars_dict)  # Converting from dictionary
print(star_wars_set)

print("* convirtiendo a un diccionario")
"""
El dict()constructor no se puede utilizar de la misma manera que los demás porque requiere pares clave-valor en lugar de solo valores. Por lo tanto, los datos deben almacenarse en un formato en el que existan pares .

Por ejemplo, una lista de tuplas donde está la longitud de cada tupla se 2puede convertir en un diccionario.

Luego, esos pares se convertirán en pares clave-valor:
"""
star_wars_list = [[1,"Anakin"], [2,"Darth Vader"], [3, 1000]]
print (star_wars_list)
star_wars_tup = ((1, "Anakin"), (2, "Darth Vader"), (3, 1000))
print (star_wars_tup)
star_wars_set = {(1, "Anakin"), (2, "Darth Vader"), (3, 1000)}
print (star_wars_set)

star_wars_dict = dict(star_wars_list) # Converting from list
print(star_wars_dict)

star_wars_dict = dict(star_wars_tup) # Converting from tuple
print(star_wars_dict)

star_wars_dict = dict(star_wars_set) # Converting from set
print(star_wars_dict)

#de entrada de muestra
my_list = [34, 82.6, "Darth Vader", 17, "Hannibal"]

#Salida de muestra
my_tuple = (34, "Hannibal", 5)
print(my_tuple)
my_tuple = (my_list[0],my_list.pop(),len(my_list))
print(my_tuple)