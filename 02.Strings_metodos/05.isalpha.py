# El método isalpha()() en Python es una función incorporada en las cadenas de texto (str) 
# que devuelve True si todos los caracteres son alfabéticos (letras, A-Z) y la cadena no 
# está vacía, retornandoFalse` en caso contrario, incluyendo números, espacios o símbolos. 
# Se utiliza frecuentemente para validar que una entrada contenga únicamente letras. 

api_data = '5'
greeting = 'Hi'
name = 'Keira McDowel'

print(api_data.isalpha()) # False
print(greeting.isalpha()) # True
print(name.isalpha())  # False  porque el espacion no es un caracter alfanumerico

print(api_data.isnumeric()) # True
print(greeting.isnumeric()) # False