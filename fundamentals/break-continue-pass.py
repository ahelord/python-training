"""
¿Qué pasa si necesitamos salir de un bucle antes de que llegue al final?

Supongamos que tenemos los primeros diez números naturales en un cuadro y tenemos que encontrar si x el número existe
en ese cuadro o no. Si x es menor que 10, no tenemos que ejecutar el bucle.

veces. Podemos parar, una vez que lo encontremos x.

Para eso break está la palabra clave. Puede romper el ciclo cuando queramos.

"""

print("* break clausula")

n = 10
x = 4
found = False  # This bool will become true once x in found

for i in range(0, n):
    if x == i+1:
        found = True
        print("Number found")
        break
    else:
        print("Number not found")

print("* continue clausula")
"""
¿Qué pasa si no queremos salir del ciclo, sino omitir todo el código en la iteración actual y pasar a la siguiente?

Para eso continue está la palabra clave. Veamos un ejemplo.
"""
for i in range(0, 10):
    if i%2 == 0:
        continue # Skipping even numbers
    print(i) # Printing odd numbers

print("* pass clausula")

colores = ["azul", "verde", "rojo"]
"""for color in colores:
    # Aqui voy a hacer algo que todavia no se # IndentationError: expected an indented block after 'for' statement on line 41 """
"""
No se puede ejecutar el codigo por que espera que se implemente el for con pass se puede evitar la implementacion
"""

for color in colores:
    # Aqui voy a hacer algo que todavia no se
    pass