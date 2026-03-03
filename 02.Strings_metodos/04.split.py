# El método .split() en Python divide una cadena de texto en una lista de subcadenas 
# basadas en un separador, siendo el espacio en blanco el valor por defecto. Es ideal
# para procesar texto, permitiendo definir un delimitador específico (como comas o guiones) 
# y el número máximo de divisiones a realizar (maxsplit).  Devuelve una lista

# Sintaxis básica: divide por espacios
frase = "Python es genial"
palabras = frase.split() 
# Resultado: ['Python', 'es', 'genial']

# Con separador personalizado
datos = "python, coding, programming, development"
lista_nombres = datos.split(",") 
# Resultado: ['python', 'coding', 'programming', 'development']

# Limitar divisiones (maxsplit)
texto = "uno,dos,tres,cuatro"
partes = texto.split(",", 2) 
# Resultado: ['uno', 'dos', 'tres,cuatro']