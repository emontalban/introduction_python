python_info = ('Python', 'Guido van Rossum', '1991', 'multiparadigma', '.py')

# Remover los elementos desde el final

python_info = python_info[:-1]
print(python_info)

# Eliminar los elementos desde el principio

python_info = python_info[1:]
print(python_info)

#Eliminar un elemento especifico (no recomendable)
# la convertimos en un lista lo borramos y despues la volvewmos a convertir en tupla

python_info = list(python_info)
python_info.remove('1991')
python_info = tuple(python_info)
print(python_info)


