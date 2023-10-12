# Supongamos que queremos encontrar el valor menor entre dos números enteros:
num1 = 10
num2 = 40
if num1 < num2:
    minimum = num1
else:
    minimum = num2
print(minimum)

num1 = 250
num2 = 120
if num1 < num2:
    minimum = num1
else:
    minimum = num2
print(minimum)

num1 = 100
num2 = 100
if num1 < num2:
    minimum = num1
else:
    minimum = num2
print(minimum)

# Todo esto podría ser mucho más sencillo si tuviéramos una función que realizara los pasos necesarios para calcular el mínimo.
minimum = min(10, 40)
print(minimum)

minimum = min(10, 100, 1, 1000)  # It even works with multiple arguments
print(minimum)

minimum = min("Superman", "Batman")  # And with different data types
print(minimum)


def my_print_function():  # No parameters
    print("This")
    print("is")
    print("A")
    print("function")


# Function ended


# Calling the function in the program multiple times
my_print_function()
my_print_function()


def minimum(first, second):
    if (first < second):
        print(first)
    else:
        print(second)


num1 = 10
num2 = 20

minimum(num1, num2)


def minimumWithReturn(first, second):
    if (first < second):
        return first
    return second


num1 = 10
num2 = 20

result = minimumWithReturn(num1, num2)  # Storing the value returned by the function
print(result)
