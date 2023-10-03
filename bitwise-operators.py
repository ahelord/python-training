

"""
Operador	Objetivo	                    Notación
&	        Bit a bit Y	                    Infijo
|	        O bit a bit	                    Infijo
^	        XOR bit a bit	                Infijo
~	        Bit a bit NO	                Prefijo
<<	        Desplazar bits a la izquierda	Infijo
>>	        Desplazar bits a la derecha	    Infijo
"""


num1 = 10  # Binary value = 01010
num2 = 20  # Binary Value = 10100

print(num1 & num2)   # 0   -> Binary value = 00000
print(num1 | num2)   # 30  -> Binary value = 11110
print(num1 ^ num2)   # 30  -> Binary value = 11110
print(~num1)         # -11 -> Binary value = -(1011)
print(num1 << 3)     # 80  -> Binary value = 0101 0000
print(num2 >> 3)     # 2   -> Binary value = 0010