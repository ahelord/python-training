"""
La comprensión de listas es una técnica que utiliza un for bucle y una condición para crear una nueva lista a partir de una existente.
El resultado es siempre una lista nueva , por lo que es una buena práctica asignar la comprensión de la lista a una nueva variable.

Una declaración de comprensión de lista siempre está entre corchetes [].

La comprensión consta de tres partes principales:

visor de svg

Es expressionuna operación utilizada para crear elementos en la nueva lista.

Iterará for loopuna lista existente. El iterador se utilizará en expression.

Los nuevos elementos sólo se agregarán a la nueva lista cuando se if conditioncumpla. Este componente es opcional.

"""
nums = [10, 20, 30, 40, 50]
nums_double = []

for n in nums:
    nums_double.append(n * 2)

print(nums)
print(nums_double)

"""
Dividamos el bucle anterior en los tres componentes de una lista por comprensión.

La expresión es equivalente a n * 2ya que se usa para crear cada valor en la nueva lista.

Nuestro forbucle es for n in numsdonde nestá el iterador.

ifEn este caso no existe una condición.

Entonces, conviertamos el bucle anterior en una lista por comprensión:
"""

nums = [10, 20, 30, 40, 50]

# List comprehension
nums_double = [n * 2 for n in nums]

print(nums)
print(nums_double)

"""
Agregar una condición 
Nuestra comprensión anterior no tenía una condición. Todos los valores de la numslista simplemente se duplicaron y agregaron nums_double.

¿Qué pasaría si solo quisiéramos que nuestra nueva lista tuviera elementos divisibles por 4?

Simplemente agregaríamos una ifcondición al final de nuestra lista de comprensión:
"""

nums = [10, 20, 30, 40, 50]

# List comprehension
# la if condition aplica a los elementos sin aplicar la expression
nums_double = [n * 2 for n in nums if n % 4 == 0]

print(nums)
print(nums_double)

print("* list comprehension con varias listas")
list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]


sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

# cada elemento de la primera lista se compara con el de la segunda lista
print(sum_list)