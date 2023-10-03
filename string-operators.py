"""
Las cadenas son compatibles con los operadores de comparación. Cada carácter tiene un valor Unicode .

Esto permite comparar cadenas en función de sus valores Unicode.

Cuando dos cadenas tienen longitudes diferentes, se dice que la cadena que aparece primero en el diccionario tiene el valor menor.
"""

print('a' < 'b')  # 'a' has a smaller Unicode value

house = "Gryffindor"
house_copy = "Gryffindor"

print(house == house_copy)

new_house = "Slytherin"

print(house == new_house)

print(new_house <= house)

print(new_house >= house)

print("* concatenar")

first_half = "Bat"
second_half = "man"

full_name = first_half + second_half
print(full_name)

#El * operador nos permite multiplicar una cadena, lo que da como resultado un patrón repetido:
print("ha" * 3)

print("* buscar")
random_string = "This is a random string"

print('of' in random_string)  # Check whether 'of' exists in randomString
print('random' in random_string)  # 'random' exists!