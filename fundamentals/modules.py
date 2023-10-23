import my_module
import sys

print(my_module.cadena_texto)
print(my_module.lista)
my_module.my_function("Hola mundo")
bmw = my_module.Coche()
print(sys.path)

from my_module import my_function, Coche
my_function("Hola mundo")
mercedes = Coche()

from my_module import *
print(cadena_texto)
print(lista)

import my_module as fundamentals
from my_module import my_function as func
fundamentals.my_function("Fundamentals")
func("Fundamentals")


