"""

Operador	Objetivo	        Notación
>	        Mas grande que	    Infijo
<       	Menos que	        Infijo
>=	        Mayor qué o igual a	Infijo
<=	        Menos que o igual a	Infijo
==	        Igual a	            Infijo
!=	        No igual a	        Infijo
is	        Igual a (identidad)	Infijo
is not	    No es igual a
            (identidad)	        Infijo

"""

"""
Los operadores ==y != comparan los valores de ambos operandos. Sin embargo, los operadores de identidad 
is y is not verifican si los dos operandos son exactamente el mismo objeto .
"""

num1 = 5
num2 = 10
num3 = 10
list1 = [6,7,8]
list2 = [6,7,8]

print(num2 > num1)  # 10 is greater than 5
print(num1 > num2)  # 5 is not greater than 10

print(num2 == num3)  # Both have the same value
print(num3 != num1)  # Both have different values

print(3 + 10 == 5 + 5)  # Both are not equal
print(3 <= 2)  # 3 is not less than or equal to 2

print(num2 is not num3)  # Both have the same object
print(list1 is list2)  # Both have the different objects

