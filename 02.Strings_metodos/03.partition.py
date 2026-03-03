# El método partition() en Python divide una cadena de texto en una tupla de
# tres elementos basándose en la primera aparición de un separador especificado. 
# Devuelve (antes, separador, después). Si el separador no se encuentra, devuelve 
# la cadena original, seguida de dos cadenas vacías. Devuelve una tupla.

heading = "Python: An Introduction"

header, _, subheader = heading.partition(': ')

print(header)
print(subheader)
#Resultado: 
#   Python
#   An Introduction

first, second, third = heading.partition(': ')

print(first)
print(second)
print(third)
# Resultado:
#   Python
#   :
#   An Introduction
