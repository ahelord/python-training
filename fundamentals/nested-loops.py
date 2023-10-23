"""
Python nos permite crear fácilmente bucles dentro de bucles. Sólo hay un inconveniente: el bucle interior siempre se completará antes que el bucle exterior.

Para cada iteración del bucle exterior, el iterador del bucle interior completará sus iteraciones para el rango dado,
 después de lo cual el bucle exterior puede pasar a la siguiente iteración.

"""

"""
Tomemos un ejemplo. Supongamos que queremos imprimir dos elementos cuya suma sea igual a un número determinado n.

La forma más sencilla sería comparar cada elemento con el resto de la lista. Un forbucle anidado es perfecto para esto:
"""

n = 50
num_list = [10, 25, 4, 23, 6, 18, 27, 47]

for n1 in num_list:
    for n2 in num_list:  # Now we have two iterators
        if(n1 != n2):
            if(n1 + n2 == n):
                print(n1, n2)
"""
La breakpalabra clave 
A veces, necesitamos salir del bucle antes de que llegue al final. Esto puede suceder si hemos encontrado lo que
 estábamos buscando y no necesitamos hacer más cálculos en el bucle.
"""
"""
Un ejemplo perfecto es el que acabamos de cubrir. En cierto punto, n1 es 23 y n2 es 27. Nuestra condición 
de n1 + n2 == nse ha cumplido. Pero los bucles siguen funcionando y comparando también todos los demás pares.
 Por eso el par se imprime dos veces. Sería bueno detenerlo cuando se encuentre el par una vez.
"""
print("* break clausula")
n = 50
num_list = [10, 25, 4, 23, 6, 18, 27, 47]
found = False  # This bool will become true once a pair is found

for n1 in num_list:
    for n2 in num_list:
        if(n1 != n2):
            if(n1 + n2 == n):
                found = True  # Set found to True
                break  # Break inner loop if a pair is found
    if found:
        print(n1, n2) # Print the pair
        break  # Break outer loop if a pair is found

print("* continue clausula")

"""
Cuando continuese utiliza la palabra clave, se omite el resto de esa iteración en particular. 
El bucle continúa hasta la siguiente iteración.
Podemos decir que no rompe el ciclo, pero omite todo el código en la iteración actual y pasa a la siguiente.
"""

num_list = list(range(0, 10))

for num in num_list:
    if num == 3 or num == 6 or num == 8:
        continue
    print(num)


print("* pass clausula ")
"""
 la pass declaración no afecta la ejecución del código. Se puede utilizar para representar un área de código 
que debe escribirse. Por lo tanto, simplemente está ahí para ayudarlo cuando no ha escrito un fragmento de código
 pero aún necesita ejecutar todo el programa.
"""

num_list = list(range(20))

for num in num_list:
    pass # You can write code here later on

print(len(num_list))