"""
Conceptos avanzados sobre funciones

En Python las funciones también se consideran objetos y como consecuencia de esto se pueden asignar a una variable,
 almacenarlas en estructuras de datos (listas, tuplas, diccionarios...) o incluso pasarlas como argumento de otras funciones.

"""

def gretting():
    print("Hola mundo")

var = gretting
var()

def func2(funcion):
    funcion()
func2(gretting)

"""
¿Qué es un decorator?
Los decorator envuelven una función, modificando su comportamiento realizando una combinación de todas las propiedades
 que hemos visto anteriormente.
"""

def greeting(): ## funcion original
    print("Hola mundo!!")

def mi_decorator(func):
    def wrapper():
        print("Ejecucion antes de la llamada a la funcion")
        func()
        print("Ejecucion despues de la llamada a la funcion")
    return wrapper

mi_funcion_mod = mi_decorator(greeting)
mi_funcion_mod()

def greeting(): ## funcion original
    print("Hola mundo!!")

def mi_decorator(func):
    def wrapper():
        if var < 5:
            func()
        else:
            print("No se puede ejecutar la funcion")
    return wrapper

funcion = mi_decorator(greeting)
var = 2
funcion()
var = 10
funcion()

print("* azucar sintactico")
"""
Python proporciona formas mas sencillas para utilizar el decorator
"""

def mi_decorator_syntactic_sugar(func):
    def wrapper():
        if var < 5:
            func()
        else:
            print("No se puede ejecutar la funcion")
    return wrapper

@mi_decorator_syntactic_sugar
def gretting_with_decorator():
    print("Hola mundo!!")

gretting_with_decorator()

print("* decoradores en clase en clases")


class Coche():
    """Esta clase representa un coche."""

    def __init__(self, modelo, potencia, consumo):
        """Inicializa los atributos de instancia.

        Argumentos posicionales:
        modelo -- string que representa el modelo del coche
        potencia -- int que representa la potencia en cv
        conumo -- int que representa el consumo en l/100km
        """
        self._modelo = modelo
        self._potencia = potencia
        self._consumo = consumo
        self._km_actuales = 0

    def especificaciones(self):
        """Muestra las especicificaciones del coche."""
        print("Modelo:", self._modelo,
              "\nPotencia: {} cv".format(self._potencia),
              "\nConsumo: {} l/100km".format(self._consumo),
              "\nKilometros actuales:", self._km_actuales)

    def actualizar_kilometros(self, kilometros):
        """Actualiza los kilometros del coche."""
        if kilometros > self._km_actuales:
            self._km_actuales = kilometros
        else:
            print("ERROR: No se puede establecer un numero de kilometros inferior al actual")

    def consumo_total(self):
        """Muestra el consumo total del coche desde el kilometro 0."""
        consumo_total = (self._km_actuales / 100) * self._consumo
        print("El consumo total es de {} litros".format(consumo_total))


class Coche():
    """Esta clase representa un coche."""

    def __init__(self, modelo, potencia, consumo):
        """Inicializa los atributos de instancia.

        Argumentos posicionales:
        modelo -- string que representa el modelo del coche
        potencia -- int que representa la potencia en cv
        conumo -- int que representa el consumo en l/100km
        """
        self._modelo = modelo
        self._potencia = potencia
        self._consumo = consumo
        self._km_actuales = 0

    def especificaciones(self):
        """Muestra las especicificaciones del coche."""
        print("Modelo:", self._modelo,
              "\nPotencia: {} cv".format(self._potencia),
              "\nConsumo: {} l/100km".format(self._consumo),
              "\nKilometros actuales:", self._km_actuales)

    @property
    def kilometros(self):
        return self._km_actuales

    @kilometros.setter
    def kilometros(self, kilometros):
        """Actualiza los kilometros del coche."""
        if kilometros > self._km_actuales:
            self._km_actuales = kilometros
        else:
            print("ERROR: No se puede establecer un numero de kilometros inferior al actual")

    def consumo_total(self):
        """Muestra el consumo total del coche desde el kilometro 0."""
        consumo_total = (self._km_actuales / 100) * self._consumo
        print("El consumo total es de {} litros".format(consumo_total))

bmw = Coche("bmw i3", 150, 6)
print(bmw.kilometros)
bmw.kilometros = 12
""" lo que hace es que se acceden como atributos globales pero son decorators que simplifican el trabajo"""
print(bmw.kilometros)

