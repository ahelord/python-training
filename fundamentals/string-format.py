"""
El formato de cadena significa sustituir valores en una cadena. A continuación se muestran algunos casos de uso de formato de cadenas:

Insertar cadenas dentro de una cadena
Insertar números enteros dentro de una cadena
Insertar flotantes dentro de una cadena
"""

string1 = "I like %s" % "Python" #Es %s el especificador de formato es porcentaje string
print(string1) # 'I like Python'

temp = "Educative"
string2 = "I like %s" % temp
print(string2) # 'I like Educative'

string3 = "I like %s and %s" % ("Python", temp)
print(string3)  # 'I like Python and Educative'

string4 = "Me gusta programar mucho en %s" % "Python"
print(string4)

string5 = """Me gusta programar
 mucho en %s""" % "Python"
print(string5)

my_string = "%i + %i = %i" % (1,2,3) # es porcentaje integer
print(my_string) # '1 + 2 = 3'

string1 = "%f" % (1.11)
print(string1) # '1.110000'

string2 = "%.2f" % (1.11)
print(string2) # '1.11'

string3 = "%.2f" % (1.117)
print(string3) # '1.12'

string3 = "%.3f" % (1.117)
print(string3) # '1.117'