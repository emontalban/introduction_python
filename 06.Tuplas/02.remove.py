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

# Diccionario con una tupla en la clave

temperaturas = {
    ('Madrid', '2026-01-01'): [10, 15, 7],
    ('Madrid', '2026-01-02'): [11, 16, 8],
    ('Bilbao', '2026-01-01'): [12, 14, 9],
    ('Bilbao', '2026-01-02'): [13, 17, 10]
}

print(temperaturas.keys())


# operador zip()

languages = ['Python', 'JavaScript','C', 'Rust', 'Java', 'C++']
years = [1991, 1995, 1972, 2010, 1995, 1985]

language_year = zip(languages, years)

print(list(language_year))






