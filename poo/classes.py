"""
Las clases son la estructura principal de la programación orientada a objetos y nos proporcionan un medio para agrupar
datos y funcionalidad. Al crear una nueva clase se crea un nuevo tipo de dato, lo que permite crear nuevas instancias de
 ese tipo que se denominan objetos. Cada instancia de clase puede tener atributos adjuntos para mantener su estado. Las
 instancias de clase también pueden tener métodos (definidos por su clase) para modificar su estado.
"""

"""
Por ejemplo cuando intentamos hacer ayuda de la clase str
Sale: Help on class str in module builtins:
"""

"""
Los nombres de las clases en Python siempre deben comenzar con una letra mayúscula. Aunque Python no fuerza que esto sea
 así a nivel sintáctico, es una convención muy importante.
"""
class Coche:
    pass

coche1 = Coche()
print(coche1)
print(type(coche1))
coche2 = Coche()
print(coche1 is coche2)

cadena1 = "Hola mundo"
cadena2 = "Adios mundo"
print(cadena1 is cadena2)

print("* parametro self")
"""
Cuando definimos métodos en una clase es necesario proporcionarles el parámetro self, que debe situarse en primer lugar
 antes de los otros parámetros. 
 El parámetro self es una referencia a la propia clase, y se utiliza para poder acceder a diferentes componentes de la misma.
"""
class Coche:
    def velocidad_maxima(self):
        """Este método devuelve la velocidad máxima del coche."""
        print("Velocidad máxima: ???")

coche3 = Coche()
coche3.velocidad_maxima()

print("* atributos de clase")
"""
Otra de las cosas que podemos definir en una clase son variables. Cuando se define una variable dentro de una clase se denomina atributo.
"""
"""
Un atributo de clase es una variable que pertenece a la clase y va a estar compartida entre todos los objetos que se instancien a partir de esa clase. 
"""
class Coche:
    atributo_clase = 150 #atributo de clase
    regulacion = 'ISO3001'

    def velocidad_maxima(self):
        """Este método devuelve la velocidad máxima del coche."""
        print("Velocidad máxima:", self.atributo_clase)

coche4 = Coche()
coche4.velocidad_maxima()

print("* atributos de instancia")

"""
Un atributo de instancia es una variable que pertenece a un objeto en particular y que solo puede ser accedida en el 
contexto de ese objeto. Estas variables deben definirse en un método especial denominado constructor y representado por
 la sintaxis __init__(). Podemos acceder al valor de estos atributos con la sintaxis:

El método __init__() es un método especial que Python ejecuta automáticamente cada vez que creamos una nueva instancia 
basada en esa clase. Este método tiene dos guiones bajos iniciales y dos guiones bajos finales, una convención que ayuda
 a evitar que los nombres de métodos por defecto de Python entren en conflicto con los definidos por el usuario.

El método __init__() se denomina constructor de la clase debido a que asigna valores específicos del objeto que se esta instanciando.
"""

class Carro:

    def __init__(self, vel_max, consumo_medio):
        self.vel_max = vel_max
        self.consumo_medio = consumo_medio

    def velocidad_maxima(self):
        print("Velocidad máxima:", self.vel_max)

    def obtener_consumo_medio(self):
        print("El consumo medio es:", self.consumo_medio)


audi = Carro(200, 7)

print(audi.vel_max)
print(audi.consumo_medio)
audi.velocidad_maxima()
audi.obtener_consumo_medio()

print("* mejora clase coche")
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

mercedes = Coche("mercedes c200", 180, 7)
mercedes.actualizar_kilometros(153_000)
mercedes.consumo_total()
