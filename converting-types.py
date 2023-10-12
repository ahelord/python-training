"""
Suede haber ocasiones en las que necesitemos cambiar datos de un tipo a otro.
En Python, este suele ser un proceso sencillo ya que el compilador puede convertir automáticamente datos entre diferentes tipos para evitar errores.
Sin embargo, existen funciones integradas que nos permiten realizar conversiones de tipos explícitas.
"""


print("* convertir int")
"""
Para convertir datos a un número entero, podemos usar la int()utilidad.

Tenga en cuenta que una cadena solo se puede convertir en un número entero si está formada por números.
"""
print(int("12") * 10)  # String to integer
print(int(20.5))  # Float to integer
print(int(False))  # Bool to integer

# print (int("Hello")) # This wouldn't work!, ValueError: invalid literal for int() with base 10: 'Hello'



print("* convertir a unicode")
"""
Esta función se puede utilizar para convertir un carácter a su valor Unicode:
"""
print(ord('a'))
print(ord('0'))

print("* convertir a float")
print(float(24))
print(float('24.5'))
print(float(True))

print("* convertir a string")
print(str(12) + '.345')
print(str(False))
print(str(12.345) + ' is a string')

print("* convertir a booleano")
"""
Las cadenas siempre se convierten a True, excepto si la cadena está vacía. Los números flotantes y enteros con un valor
de cero se consideran False en términos booleanos:
"""
print(bool(10))
print(bool(0.0))
print(bool("Hello"))
print(bool(""))

