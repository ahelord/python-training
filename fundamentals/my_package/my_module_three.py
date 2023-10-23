def func():
    print("Hello world from my module 3")

"""
es el __name__ muestra si el archivo se ejecuta o es llamado desde importacion lo que 
permite ajustar el comportamiento para un caso o para el otro
"""
if __name__ == '__main__':
    print("me estan ejecutando directamente")