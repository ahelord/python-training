"""
Buscar
Una alternativa para encontrar una subcadena usando la inpalabra clave es el find()método. Devuelve el primer índice en el que aparece una subcadena en una cadena. Si no se encuentra ninguna instancia de la subcadena, el método devuelve -1.

-1es un valor convencional que representa un Nonefallo en caso de que se supusiera que la salida fuera positiva.

Para una cadena llamada a_string, find()se puede utilizar de la siguiente manera:

a_string.find(substring, start, end)
substring es lo que estamos buscando.
start es el índice desde el que empezamos a buscar a_string.
end es el índice donde detenemos nuestra búsqueda a_string.
start y endson opcionales.
"""
print("* Buscar")
random_string = "This is a string"
print(random_string.find("is"))  # First instance of 'is' occurs at index 2
print(random_string.find("is", 9, 13))  # No instance of 'is' in this range


"""
El replace()método se puede utilizar para reemplazar una parte de una cadena con otra cadena. Aquí está la plantilla que debemos utilizar:

a_string.replace(substring_to_be_replaced, new_string)
"""
print("* reemplazar")
a_string = "Welcome to Educative!"
new_string = a_string.replace("Welcome to", "Greetings from")
print(a_string)
print(new_string)

"""
En Python, las letras entre mayúsculas y minúsculas de una cadena se pueden cambiar fácilmente usando los métodos upper()y lower().
"""
print("* mayusculas minusculas")

print("UpperCase".upper())
print("LowerCase".lower())

print("* unir cadenas")
llist = ['a', 'b', 'c']
print('>>'.join(llist)) # joining strings with >>
print('<<'.join(llist)) # joining strings with <<
print(', '.join(llist)) # joining strings with comma and space

print("* formato")

"""
El format() método se puede utilizar para formatear los valores especificados e insertarlos en los marcadores de 
posición de la cadena. Probémoslo:
"""
string1 = "Learn Python {version} at {cname}".format(version = 3, cname = "Educative")
string2 = "Learn Python {0} at {1}".format(3, "Educative")
string3 = "Learn Python {} at {}".format(3, "Educative")

print(string1)
print(string2)
print(string3)