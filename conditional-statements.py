"""
if condtional statement is True:
    # execute expression1
    pass
else:
    # execute expression2
    pass

    """

"""
Hay tres tipos de declaraciones condicionales en Python:

if
if-else
if-elif-else
"""


"""
La sangría juega un papel esencial en Python. Las declaraciones con el mismo nivel de sangría pertenecen al mismo
 bloque de código. El código de una ifdeclaración tiene una sangría un espacio más que el código exterior para indicar 
 que se trata de un bloque interno e interrelacionado .
"""

#si la condición se cumple True, ejecute el código a ejecutar . De lo contrario, sáltatelo y continúa.

num = 5

if num == 5:  # The condition is true
    print("The number is equal to 5")  # The code is executed

if num > 5:  # The condtion is false
    print("The number is greater than 5")  # The code is not executed

num = 12

if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
    # Only works when num is a multiple of 2, 3, and 4
    print("The number is a multiple of 2, 3, and 4")

if (num % 5 == 0 or num % 6 == 0):
    # Only works when num is either a multiple of 5 or 6
    print("The number is a multiple of 5 and/or 6")

num = 63

if num >= 0 and num <= 100:
    if num >= 50 and num <= 75:
        if num >= 60 and num <= 70:
            print("The number is in the 60-70 range")
num = 10
if num > 5:
    num = 20  # Assigning a new value to num
    new_num = num * 5  # Creating a new value called newNum

# The if condition ends, but the changes made inside it remain
print(num)
print(new_num)


print("* Declaracion if-else")

num = 60

if num <= 50:
    print("The number is less than or equal to 50")
else:
    print("The number is greater than 50")

print("* expresion condicional")
num = 60

output = "The number is less than or equal to 50" if num <= 50 else "The number is greater than 50"

print(output)

print("* Declaracion if-elif-else")
light = "Red"

if light == "Green":
    print("Go")
elif light == "Yellow":
    print("Caution")
elif light == "Red":
    print("Stop")
else:
    print("Incorrect light signal")

# elif puede existir sin else
if light == "Green":
    print("Go")
elif light == "Yellow":
    print("Caution")
elif light == "Red":
    print("Stop")

num = 5

if num == 0:
    print("Zero")
elif num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
elif num == 4:
    print("Four")
elif num == 5:
    print("Five")
elif num == 6:
    print("Six")
elif num == 7:
    print("Seven")
elif num == 8:
    print("Eight")
elif num == 9:
    print("Nine")



print("* ejercicio")

"""
En este desafío deberás descontar un precio según su valor.

Si el precio es 300o superior, habrá un 30%descuento.

Si el precio está entre 200y 300( 200incluido), habrá 20%descuento.

Si el precio está entre 100y 200( 100incluido), habrá 10%descuento.

Si el precio es inferior a 100, habrá un 5%descuento.

Si el precio es negativo no habrá descuento.
"""
price = 250

if price<0:
    price=0
elif price>=300:
    price-=price*0.3
elif price< 299 and price>=200:
    price-=price*0.2
elif price< 199 and price>=100:
    price-=price*0.1
elif price< 100:
    price-=price*0.05

print(price)
