"""
Una tupla es muy similar a una lista, excepto por el hecho de que su contenido no se puede cambiar.
En otras palabras, una tupla es inmutable . Sin embargo, puede contener elementos mutables como una lista.
Estos elementos pueden modificarse.

El contenido de una tupla está entre paréntesis (). También están ordenados y, por tanto, siguen la notación de índice lineal.
"""
car = ("Ford", "Raptor", 2019, "Red")
print(car)

# Length
print(len(car))

# Indexing
print(car[1])

# Slicing
print(car[2:])

# car[2]=1 TypeError: 'tuple' object does not support item assignment

print("* fusionando tuplas")
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = hero1 + hero2
print(awesome_team)

print("* tuplas anidadas")
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero1, hero2)
print(awesome_team)

print("* buscar en una tupla")
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Moscow" in cities)

cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(cities.index("Tokyo"))

