"""
El whilebucle sigue iterando sobre un determinado conjunto de operaciones mientras se cumpla una determinada condición True .

Opera usando la siguiente lógica:

Mientras esta condición sea cierta, mantenga el ciclo en ejecución.
"""
print("* while bucle")

"""
Aquí hay un while bucle que descubre la potencia máxima de n antes de que el valor exceda 1000:
"""
n = 2  # Could be any number
power = 0
val = n
while val < 1000:
    power += 1
    val *= n

print(power)

"""
También podemos usar while bucles con estructuras de datos, 
especialmente en los casos en que la longitud de la estructura de datos cambia durante las iteraciones.

El siguiente bucle calcula la suma del primer y último dígito de cualquier número entero:
"""

n = 249
last = n % 10  # Finding the last number is easy

first = n  # Set it to `n` initially
while first >= 10:
    first //= 10  # Keep dividing by 10 until the leftmost digit is reached.

result = first + last
print(result)


print("* ciclos infinitos")
"""while (True):
    print("Hello World")
"""
"""x = 1
while(x > 0):
    x += 5
    print(x)"""


"""
Las palabras clave , y funcionan con bucles break.continuepasswhile

Al igual que forlos bucles, también podemos anidar whilebucles. Además, podemos anidar los dos tipos de bucles entre sí.
"""