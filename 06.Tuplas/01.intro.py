# Las tuplas son secuencias ordenadas e inmutables de elementos en Python,
# definidas con paréntesis (), utilizadas para almacenar datos constantes. 
# A diferencia de las listas ([]), que son mutables (modificables), 
# las tuplas no permiten añadir, eliminar o cambiar elementos una vez creadas, 
# lo que las hace más eficientes en memoria y velocidad.

python_info = ("Python", "Guido van Rossum", "1991")

# se puede asignar cada elemento a una variable en las listas como en las tuplas 
# pero las tuplas con inmutables no se pueden modificar

name, creator, year = python_info
print(name)
print(creator)
print(year)

print('***************************************')

# lo mismo accediendo al indice
name = python_info[0]
creator = python_info[1]
year = python_info[2]
print(name)
print(creator)
print(year)

# Una tupla no se puede modificar, pero sí se puede crear una nueva tupla y reasignarla a la misma variable.
# para añadir mas elementos a las tuplas hay que reasignarlo
# para que pueda concatenar es importante que acabe en una coma
python_info = python_info + ('multiparadigma',)
print(python_info)

# tambien podemos añadir el operador +=
python_info += ('.py',)
print(python_info)

libraries = ["NumPy", "Pandas", "Matplotlib"]
python_info += (libraries,)

python_info += (["Django", "Flask", "FastAPI"],)
print(python_info)

# para acceder a flask
print(python_info[6][1]) # Flask
print(python_info[-1][1]) # Flask
