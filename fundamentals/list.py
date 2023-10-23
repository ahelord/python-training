"""
La lista es quizás la estructura de datos más utilizada en Python.
Nos permite almacenar elementos de diferentes tipos de datos en un contenedor.
El contenido de una lista está entre corchetes, [].

Las listas están ordenadas, como cadenas. Los elementos se almacenan linealmente en un índice específico .

"""

jon_snow = ["Jon Snow", "Winterfell", 30]
print(jon_snow)

# Indexing
print(jon_snow[0])

# Length
print(len(jon_snow))

jon_snow = ["Jon Snow", "Winterfell", 30]
print(jon_snow[2])
jon_snow[2] += 3
print(jon_snow[2])

num_seq = range(0, 10)  # A sequence from 0 to 9
num_list = list(num_seq)  # The list() method casts the sequence into a list
print(num_list)

num_seq = range(3, 20, 3)  # A sequence from 3 to 19 with a step of 3
print(list(num_seq))

world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners)


print("* indexacion secuencial")
world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners[1])
print(world_cup_winners[1][1])  # Accessing 'Spain'
print(world_cup_winners[1][1][0])  # Accessing 'S'

print("* funcionar listas")
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
merged_list = part_A + part_B
print(merged_list)

print("* extender lista")
"""
Alternativamente, podríamos usar la extend()propiedad de una lista para agregar los elementos de una lista al final de otra:
"""
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
part_A.extend(part_B)
print(part_A)

print("* operaciones lista")

print("* append agregar un elemento")
"""
Agregar elementos 
No siempre se pueden especificar todos los elementos de una lista de antemano y existe una gran posibilidad de que queramos agregar más elementos durante el tiempo de ejecución.

El append()método se puede utilizar para agregar un nuevo elemento al final de un archivo list. Se debe seguir el siguiente modelo:
a_list.append(newElement)

"""
num_list = []  # Empty list
num_list.append(1)
num_list.append(2)
num_list.append(3)
print(num_list)

print("* agregar un elemento a un indice particular")
"""
Para agregar un elemento en un índice particular de la lista, podemos usar el insert()método. Lo usaremos en el siguiente formato:

aList.insert(index, newElement)

Si ya existe un valor en ese índice, toda la lista a partir de ese valor se desplazará un paso hacia la derecha:
"""

num_list = [1, 2, 3, 5, 6]
num_list.insert(3, 4)  # Inserting 4 at the 3rd index. 5 and 6 shifted ahead
print(num_list)
num_list.insert(20, 4)  # if index not exist object added to final
print(num_list)

print("* eliminado elementos de una lista")
print("* pop")
"""
es la pop()operación que elimina el último elemento de la lista.
"""

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
last_house = houses.pop()
print(last_house)
print(houses)


print("* remove")
"""
Si necesitamos eliminar un valor particular de una lista, podemos usar el remove()método siguiendo esta plantilla:
aList.remove(element_to_be_deleted)

"""
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
print(houses)
houses.remove("Ravenclaw")
print(houses)

# For nested lists
populations = [["Winterfell", 10000], ["King's Landing", 50000],
               ["Iron Islands", 5000]]
print(populations)
populations.remove(["King's Landing", 50000])
print(populations)

print("* cortar lista")

"""
La división de listas es el término utilizado para obtener una parte de una lista dados los índices inicial y final.

"""
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list[2:5])
print(num_list[0::2])

print("* buscar indice")
"""
Con las listas es realmente fácil acceder a un valor a través de su índice. Sin embargo, también es posible la operación contraria donde podemos encontrar el índice de un valor determinado.
"""
cities = ["London", "Paris", "Los Angeles", "Beirut"]
print(cities.index("Los Angeles"))  # It is at the 2nd index

print("* verificar la existencia de un elemento dentro de la lista")
"""
Si solo queremos verificar la existencia de un elemento en una lista, podemos usar el inoperador:
"""
cities = ["London", "Paris", "Los Angeles", "Beirut"]
print("London" in cities)
print("Moscow" not in cities)

print("* ordenar lista")
"""
Una lista se puede ordenar en orden ascendente utilizando el sort()método. La clasificación se puede realizar alfabética o numéricamente según el contenido de la lista:
"""
num_list = [20, 40, 10, 50.4, 30, 100, 5]
num_list.sort()
print(num_list)