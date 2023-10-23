"""
Cuando pensamos en un diccionario, lo que aparece es la imagen de un libro enorme que contiene palabras con sus significados.

En términos más simples, la información se almacena en pares de palabras y significados. La estructura de datos del
diccionario de Python sigue la misma estructura.

Un diccionario almacena pares clave-valor , donde cada clave única es un índice que contiene el valor asociado a ella.


Los diccionarios están desordenados porque las entradas no se almacenan en una estructura lineal.

En Python, debemos poner el contenido del diccionario entre llaves {}:
Un par clave-valor se escribe en el siguiente formato:

key:value

"""
empty_dict = {}  # Empty dictionary
print(empty_dict)

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

"""
Nota : dado que el diccionario es una estructura de datos desordenada, el orden de salida no necesariamente
 coincidirá con el orden en el que escribimos las entradas. Se accede a los pares clave-valor de forma aleatoria o desordenada .


El dict()constructor 
Como sugiere el nombre, el dict()constructor se puede utilizar para construir un diccionario. Piense en el "constructor" como una operación que nos proporciona un diccionario.

Si nuestras claves son cadenas simples sin caracteres especiales, podemos crear entradas en el constructor. En ese caso, los valores se asignarán a las claves mediante el =operador.

Una práctica popular es crear un diccionario vacío y agregar entradas más tarde.

Refactoricemos los ejemplos empty_dicty phone_bookpara que funcionen con dict():

"""

empty_dict = dict()  # Empty dictionary
print(empty_dict)

phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# Keys will automatically be converted to strings
print(phone_book)

# Alternative approach
phone_book = dict([('Batman', 468426),
                   ('Cersei', 237734),
                   ('Ghostbusters', 44678)])
print(phone_book)

"""
Las claves y los valores pueden tener cualquiera de los tipos o estructuras de datos básicos.

Dos claves pueden tener el mismo valor. Sin embargo, es crucial que todas las claves sean únicas .

Podemos ver en el phone_bookejemplo cómo los diccionarios pueden organizar datos de manera significativa. Es fácil saber el número de teléfono de un personaje porque el par se almacena junto.
"""

print("* accediendo a los valores")

"""
Para muchos, aquí es donde un diccionario tiene ventaja sobre una lista o una tupla. Como no hay índices lineales, no necesitamos realizar un seguimiento de dónde se almacenan los valores.

En su lugar, podemos acceder a un valor encerrando su clave entre corchetes, []. Esto es más significativo que los índices enteros que usamos para tuplas y listas.

Alternativamente, podemos usar el get() método de la siguiente manera:

a_dictionary.get(key)
"""

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book["Cersei"])
print(phone_book.get("Ghostbusters"))


print("* agregar y actualizar entradas")
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

phone_book["Godzilla"] = 46394  # New entry
print(phone_book)

phone_book["Godzilla"] = 9000  # Updating entry
print(phone_book)

print("* borrando entradas")
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

del phone_book["Batman"]
print(phone_book)

"""
Si queremos utilizar el valor eliminado, los métodos pop()o popitem()funcionarían mejor:
"""
print("* utilizar el valor eliminado")
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

cersei = phone_book.pop("Cersei")
print(phone_book)
print(cersei)

# Removes and returns the last inserted pair, as a tuple
# In Python versions before 3.7, popitem() removes and returns the random item
lastAdded = phone_book.popitem()
print(lastAdded)

print("* longitud de un diccionario")
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(len(phone_book))

print("* comprobando la existencia de una clave")
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print("Batman" in phone_book)
print("Godzilla" in phone_book)

print("* copiar contenido")
"""
Para copiar el contenido de un diccionario a otro, podemos utilizar la update()operación:

"""
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}

second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}

# Add secondphone_book to phone_book
phone_book.update(second_phone_book)
print(phone_book)

print("* compresion de diccionario")
"""
Python también admite la comprensión de diccionarios, que funcionan de manera muy similar a las listas de comprensión. Crearemos nuevos pares clave-valor basados ​​en un diccionario existente.

Sin embargo, para iterar el diccionario, usaremos la dict.items()operación que convierte un diccionario en una lista de (key, value)tuplas.

A continuación se muestra un ejemplo sencillo en el que las claves del diccionario original se elevan al cuadrado y '!'se añaden a cada valor de cadena:
"""

houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
# el : representa la llave balor
new_houses = {n**2: house + "!" for (n, house) in houses.items() if house=="Ravenclaw"}
print(houses)
print(new_houses)

print("* definir key de diccionarios como tuplas")
dic3 = {
    ("uno", 1): "one",
    ("dos", 2): "two",
    ("tres", 3): "three"
}
print(dic3[("uno", 1)])