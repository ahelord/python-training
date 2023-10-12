"""
Tenemos que especificar los nombres de las funciones mientras las creamos.
Sin embargo, existe una clase especial de funciones para las que no necesitamos especificar nombres de funciones.
"""
"""
Definición 
Una lambda es una función anónima que devuelve algún tipo de datos.

Las lambdas se definen mediante la lambda palabra clave. Dado que devuelven datos, es una buena práctica asignarlos a una variable.

lambda parameters:expresion

En la estructura anterior, son parameter sopcionales.
"""

"""
A continuación podemos encontrar una lambda que triplica el valor del parámetro y devuelve este nuevo valor:

"""
triple = lambda num : num * 3  # Assigning the lambda to a variable

print(triple(10)) # Calling the lambda and giving it a parameter


"""
Aquí hay una lambda simple que concatena los primeros caracteres de tres cadenas:
"""
concat_strings = lambda a, b, c: a[0] + b[0] + c[0]
print(concat_strings("World", "Wide", "Web"))


"""
Como podemos ver, las lambdas son más simples y legibles que las funciones normales. Pero esta simplicidad tiene una limitación.

Una lambda no puede tener una expresión de varias líneas. Esto significa que nuestra expresión debe ser algo que pueda escribirse en una sola línea.

Por lo tanto, las lambdas son perfectas para funciones cortas de una sola línea.

También podemos usar declaraciones condicionales dentro de lambdas:
"""

my_func = lambda num: "High" if num > 50 else "Low"

print(my_func(60))

"""
Cuando se utilizan declaraciones condicionales en lambdas, el par if- elsees necesario.
 Es necesario cubrir ambos casos; de lo contrario, la lambda arrojará un error:
"""
"""
my_func = lambda num: "High" if num > 50 # expected 'else' after 'if' expression
"""
