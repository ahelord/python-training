print("* Recursion")

"""
Una cosa a tener en cuenta es que una llamada externa no puede avanzar hasta que hayan finalizado todas las llamadas
 recursivas internas. Es por eso que obtenemos una secuencia de 5to 0to 5.
"""

def rec_count(number):
    print("*",number)
    # Base case
    if number == 0:
        return 0
    rec_count(number - 1)  # A recursive call with a different argument
    print("-",number)


rec_count(5)

print("* Fibonacci")
def fib(n):
    # The base cases
    if n <= 1:  # First number in the sequence
        return 0
    elif n == 2:  # Second number in the sequence
        return 1
    else:
        # Recursive call
        return fib(n - 1) + fib(n - 2)


print(fib(6))

print("* exercise")

"""
En este ejercicio, debes implementar la rep_catfunción. Se le dan dos números enteros xy y, como argumentos. 
Debes convertirlos en cadenas. El valor de cadena de xdebe repetirse 10veces y el valor de cadena de ydebe repetirse 5veces.

Al final, yse concatenará xy se deberá devolver la cadena resultante

Número de entrada de muestra
x = 3
y = 4
Salida de muestra 

'333333333344444'


"""
def rep_cat(x, y):
    # Write your code here
    return str(x)*10 + str(y)*5
print(rep_cat(3,4))