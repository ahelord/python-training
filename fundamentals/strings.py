print("Harry Potter!")  # Double quotation marks

got = 'Game of Thrones...'  # Single quotation marks
print(got)
print("$")  # Single character

empty = ""
print(empty)  # Just prints an empty line

multiple_lines = '''Triple quotes allows
multi-line string.''' #Para agregar una cadena de varias líneas podemos usar comillas triples.
print(multiple_lines)


#Tamaño de cadena
print("* Tamaño de cadena")
random_string = "I am Batman"  # 11 characters
print(len(random_string))



#Indice de un string
print("* Indice de un string")
batman = "Bruce Wayne"

first = batman[0]  # Accessing the first character
print(first)

space = batman[5]  # Accessing the empty space in the string
print(space)

last = batman[len(batman) - 1]
print(last)
# The following will produce an error since the index is out of bounds
#err = batman[len(batman)]

print("* Indexacion inversa")
batman = "Bruce Wayne"
print(batman[-1])  # Corresponds to batman[10]
print(batman[-5])  # Corresponds to batman[6]

print("* Inmutabilidad de cadenas")
string = "Immutability"
#string[0] = 'O' # Will give error El código anterior se debe TypeErrora que Python no admite la asignación de elementos en el caso de cadenas.

# Cuando cambio el valor de un string estoy en realidad reemplazado la variable con otra variable del mismo nombre

str1 = "hello"
print(id(str1))
print(str1)
str1 = "bye"
print(id(str1))
print(str1)


print("* Cortar string")

my_string = "This is MY string!"
print(my_string[0:4]) # From the start till before the 4th index
print(my_string[1:7])
print(my_string[8:len(my_string)-1]) # From the 8th index till the end

print("* Cortar con paso")
my_string = "This is MY string!"
print(my_string[0:7])  # A step of 1
print(my_string[0:7:2])  # A step of 2
print(my_string[0:7:5])  # A step of 5

print("* Cortar con paso inverso")
my_string = "This is MY string!"
print(my_string[13:2:-1]) # Take 1 step back each time
print(my_string[17:0:-2]) # Take 2 steps back. The opposite of what happens in the slide above
print(my_string[len(my_string):2:-1]) # Take 1 step back each time

print("* Cortar parcial")
my_string = "This is MY string!"
print(my_string[:8])  # All the characters before 'M'
print(my_string[8:])  # All the characters starting from 'M'
print(my_string[:])  # The whole string
print(my_string[::-1])  # The whole string in reverse (step is -1)