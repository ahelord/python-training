"""
Los paquetes permiten estructurar jerárquicamente los módulos que hemos definido.

Para inicializar un directorio dentro de nuestro sistema operativo y que Python lo reconozca como un paquete que contiene módulos que pueden importarse, debe crearse un fichero dentro del directorio con el nombre __init__.py.

El código de __init__.py se invocará cuando el paquete o un módulo del paquete sea imortando en el programa. Esto puede utilizarse para establecer código de inicialización de los paquetes o de los módulos.

Para importar un módulo que se encuentra en un paquete debe utilizarse la sintaxis:


import <nombre_paquete>.<nombre_modulo>

from <nombre_paquete>.<nombre_modulo> import <nombre(s)>
"""

print(" Se ha importado un modulo de my_package")

# Dentro del fichero __init__.py del modulo
__all__ = [
    'my_module_two','my_module_three'
]