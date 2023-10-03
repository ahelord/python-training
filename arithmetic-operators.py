"""
A continuación, podemos encontrar los operadores aritméticos básicos en orden de precedencia . El operador que figura más arriba se calculará primero.

Estos operadores nos permiten realizar operaciones aritméticas en Python.

Operador	Objetivo	                                        Notación
()	        Paréntesis	                                        Encapsula la operación precedente
**	        Exponente	                                        Infijo
%, *, /,//	Módulo, multiplicación, división, división de piso	Infijo
+,-	        Suma resta	                                        Infijo

"""

print("* Suma")
print(10 + 5)

float1 = 13.65
float2 = 3.40
print(float1 + float2)

num = 20
flt = 10.5
print(num + flt)

print("* Resta")

print(10 - 5)

float1 = -18.678
float2 = 3.55
print(float1 - float2)

num = 20
flt = 10.5
print(num - flt)

print("* multiplicacion")
print(40 * 10)

float1 = 5.5
float2 = 4.5
print(float1 * float2)

print(10.2 * 3)

print("* division")
print(40 / 10)

float1 = 5.5
float2 = 4.5
print(float1 / float2)
print(12.4 / 2) #Una operación de división siempre da como resultado un número de punto flotante.

print("* division de piso")
"""En la división de piso, el resultado se reduce al número entero más pequeño más cercano. 
También se conoce como división de números enteros ."""

print(43 // 10)

float1 = 5.5
float2 = 4.5
print(5.5 // 4.5)
print(12.4 // 2)

print("* modulo")
print(10 % 2)

twenty_eight = 28
print(twenty_eight % 10)

print(-28 % 10)  # The remainder is positive if the right-hand operand is positive
print(28 % -10)  # The remainder is negative if the right-hand operand is negative
print(34.4 % 2.5)  # The remainder can be a float

print("* precedencia")
# Different precedence
print(10 - 3 * 2)  # Multiplication computed first, followed by subtraction

# Same precedence
print(3 * 20 / 5)  # Multiplication computed first, followed by division
print(3 / 20 * 5)  # Division computed first, followed by multiplication

print("* parantesis")
print((10 - 3) * 2)  # Subtraction occurs first
print((18 + 2) / (10 % 8))