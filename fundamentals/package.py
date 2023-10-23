"""
Los paquetes permiten estructurar jerárquicamente los módulos que hemos definido.

Para inicializar un directorio dentro de nuestro sistema operativo y que Python lo reconozca como un paquete que contiene módulos que pueden importarse, debe crearse un fichero dentro del directorio con el nombre __init__.py.

El código de __init__.py se invocará cuando el paquete o un módulo del paquete sea imortando en el programa. Esto puede utilizarse para establecer código de inicialización de los paquetes o de los módulos.

Para importar un módulo que se encuentra en un paquete debe utilizarse la sintaxis:


import <nombre_paquete>.<nombre_modulo>

from <nombre_paquete>.<nombre_modulo> import <nombre(s)>

Ya no se necesita el __init__ desde las 3.3 pero podria ser util para definir codigo de inicializacion
"""

from my_package.my_module_two import func_two
func_two()

print("importar todos los modulos de un paquete")

"""
Python sigue la siguiente convención: si el archivo __init__.py en el directorio del paquete contiene una lista llamada __all__, se toma como una lista de módulos que deben ser importados cuando se encuentra la sentencia:
"""
from my_package import *
my_module_three.func()
my_module_two.func_two()

"""
Asi se pueden importar subpaquetes dentro de paquetes
from <nombre_paquete>.<nombre_subpaquete>.<nombre_modulo> import <nombre(s)>

"""