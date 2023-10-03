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