#Boleans
#Es un valor verdadero o falso

is_active = False

print(is_active)

#Number - almacena numeros

age = 34
prize = 19.99
number = 2 + 3j

print(age, prize, number)


#String - almacena cualquier tipo de cadena de caracteres

name = 'Keira'
message ="Hola Mundo"

print(name, message)

# Bytes and byte arrays
# Se usan para trabajar con datos binarios (archivos, redes, imágenes).

date_byte= b'Hola' #inmutable

date_byte_array = bytearray(5) #mutable

print(date_byte, date_byte_array)

#None - Representa la ausencia de valor - se usa cuando algo no tiene valor todavia

result = None
print(result)

#Lists - Coleccion ordenada y mutable []

names = ["Anna", "Louis", "Peter"]

print (names)

#Tuples - Coleccion ordenada pero inmutable ()

colors = ("red", "green", "blue")

print (colors)

#Sets - Conjuntos - Coleccion no ordenada y sin duplicados {}

numbers_set = {1, 2, 3, 3, 4}

print(numbers_set)  # {1, 2, 3, 4} → elimina duplicados {}

#Dict - Coleccion de pares clave:valor

person = {
    "name": "Keira",
    "age": 54,
    "city": "Madrid"
}

print(person)


