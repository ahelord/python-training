"""
El alcance de una función significa el grado en que las variables y otros elementos de datos creados dentro de la función son accesibles en el código.

En Python, el alcance de la función es el cuerpo de la función.

Cada vez que se ejecuta una función, el programa pasa al alcance de la función. Regresa al alcance exterior una vez que la función ha finalizado.
"""
"""
En Python, los datos creados dentro de la función no se pueden utilizar desde el exterior a menos que sean devueltos por la función.
Las variables de una función están aisladas del resto del programa. Cuando finaliza la función, se liberan de la memoria y no se pueden recuperar.
"""
"""
def func():
    name = "Stark"


func()
print(name)  # Accessing 'name' outside the function
"""
"""
De manera similar, la función no puede acceder a datos fuera de su alcance a menos que los datos se hayan pasado como argumento.
"""
name = "Ned"
def func():
    name = "Stark"

func()
print(name)  # The value of 'name' remains unchanged.

"""
Alteración de datos 
Cuando se pasan datos mutables a una función, la función puede modificarlos o alterarlos. Estas modificaciones también 
permanecerán vigentes fuera del alcance de la función. Un ejemplo de datos mutables es una lista.

En el caso de datos inmutables , la función puede modificarlos, pero los datos permanecerán sin cambios fuera del
 alcance de la función. Ejemplos de datos inmutables son números, cadenas, etc.

Intentemos cambiar el valor de un número entero dentro de una función:
"""
num = 20


def multiply_by_10(n):
    n *= 10
    num = n  # Changing the value inside the function
    print("Value of num inside function:", num)
    return n


multiply_by_10(num)
print("Value of num outside function:", num)  # The original value remains unchanged

"""
Si realmente necesitamos actualizar variables inmutables a través de una función, simplemente podemos 
asignar el valor de retorno de la función a la variable.
"""

num_list = [10, 20, 30, 40]
print(num_list)


def multiply_by_10(my_list):
    my_list[0] *= 10
    my_list[1] *= 10
    my_list[2] *= 10
    my_list[3] *= 10


multiply_by_10(num_list)
print(num_list)  # The contents of the list have been changed

"""
Pasamos num_lista nuestra función como my_listparámetro. Ahora, cualquier cambio realizado my_listse reflejará num_listfuera de la función. Esto no sucedería en el caso de una variable inmutable.

En este punto, comprendemos mejor el alcance de una función.
"""