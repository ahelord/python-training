"""
Un Namespace es un mapeo de nombres a objetos. Los Namespaces se crean en diferentes momentos y tienen diferentes tiempos de vida.
"""

"""
Nombres de palabras claves de python
"""
print("* namespace por defecto")
print(dir(__builtins__))

"""
El Namespace global para un módulo se crea cuando se lee la definición del módulo y, normalmente, dura hasta que el intérprete se cierra.
"""
var_modulo = 10
print("* namespace por global")
print(globals())

"""
El Namespace local para una función o cualquier otra estructura de Python se crea cuando se llama a la función, 
y se borra cuando la función termina. Las invocaciones recursivas tienen cada una su propio Namespace.
"""
print("*namespace local")
def func():
    var_local_func = 5
    var_local_func = 10
    print(locals())
func()

"""
Scope: El scope es una región de un programa en Python donde un Namespace es directamente accesible.

En Python existen diferentes scopes desde los que se puede acceder a los Namespaces con algunas particularidades que debemos tener en cuenta:
"""

"""
Scope local
El scope local (o de función) es el bloque de código o cuerpo de cualquier función o expresión en Python. Contiene los nombres que se definen
 dentro de la función. Estos nombres sólo serán visibles desde el código de la función. Se crea en la llamada a la función, 
 no en la definición de la misma, por lo que habrá tantos scopes locales diferentes como llamadas a la función.
"""
print("*scope scope local")
def func():
    var_local_func = 10
    print(var_local_func)
func()

print("* scope no local  ")
"""
Deciamos entonces que el cuerpo de la funcion es el namespece local pero ahora que pasa cuando ahi dos funciones.

En python se decidio que lo que esta anidado se le llama scope local y la externa se le denomima scope no local

"""
def func():
    var_no_local_func = 10
    print("Namespace func", locals())
    def func2():
        var_local_func2 = 5
        print("Namespace func2", locals())
    func2()

func()

"""
La pregunta seria en que forma puedo acceder al namespace local o no local?
"""
def func():
    var_no_local_func = 10
    def func2():
        var_local_func2 = 5
        print(var_no_local_func) # siempre que las variables que se definan en un scope superior se pueden acceder en scope inferiores
    func2()

func()


"""def func():
    var_no_local_func = 10
    print(var_local_func2) # siempre que las variables que se definan en un scope inferior no se pueden acceder en scope superior
    def func2():
        var_local_func2 = 5
    func2()"""

print("* scope global")

"""
El scope global (o de módulo) es el ámbito superior de un programa, script o módulo de Python. Este ámbito de Python 
contiene todos los nombres que se definen en el nivel superior de un programa o módulo. Los nombres en este ámbito de Python son visibles desde cualquier parte de tu código.
"""

var_global = 15
print(var_global)
def func3():
    def func4():
        print(var_global)
    func4()
func3()

print("* scope por defecto")
"""
El scope por defecto es un ámbito especial de Python que se crea o carga cada vez que ejecutas un script o abres una 
sesión interactiva. Este ámbito contiene nombres como palabras clave, funciones, excepciones y otros atributos que están 
incorporados en Python. Los nombres en este ámbito de Python también están disponibles desde cualquier parte de tu código.
 Es cargado automáticamente por Python cuando ejecutas un programa o script.
"""
def func():
    True

def func():
    def func2():
        True
    func2()

"""
Una de las cosas importantes es que los nombres que se encuentran en un scope determinado puede ser accedidos desde un 
scope externo pero no pueden ser actualizados o modificados
"""
"""contador = 0
def actualizar_contador():
    contador += 1 #UnboundLocalError: cannot access local variable 'contador' where it is not associated with a value

print(actualizar_contador())"""

print("* sentencias global")
"""
Teniendo en cuenta el comportamiento por defecto que hemos visto en los apartados anteriores, Python nos proporciona
 las dos sentencias global y nonlocal para modificarlo si lo necesitásemos.
"""
contador = 0
def actualizar_contador():
    global contador # Indica que la variable esta en el namespace global y no local
    contador += 1
actualizar_contador()
print(contador)

print("* sentencias nonlocal")
def funcion():
    contador = 0
    def actualizar_contador():
        nonlocal contador
        contador += 1
    actualizar_contador()
    print(contador)

funcion()


"""
No esta recomendado utilizar global y nolocal
"""
