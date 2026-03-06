programming_languages = ["Python", "Java", "C++","JavaScript","Ruby","Go","Rust","C#","Swift","Kotlin"]
# El método sort() en Python sirve para ordenar los elementos de una lista.
# Ordena los textos alfabéticamente
# Ordena los números de menor a mayor por defecto.
# No se puede almacenar el resultado en una variable

programming_languages.sort()
print(programming_languages)


# Puedes ordenar de mayor a menor usando reverse=True.

programming_languages.sort(reverse=True)
print(programming_languages)

# Podemos ordenar una lista de strings por la longitud de cada palabra. (key = len)

programming_languages.sort(key=len)
print(programming_languages)

# Cuando hay mayusculas y minusculas en la primera letra sort() puede dar un resultado raro
# ya que primero ordenara por mayusculas y luego por minusculas
# para evitar eso usamos (key=str.lower)

programming_languages.sort(key=str.lower)
print(programming_languages)

# El método .join() se utiliza para concatenar (unir) todos los elementos de una lista
# en una sola cadena de texto. Se aplica a una cadena separadora, colocando dicho separador 
# entre cada elemento, siendo ideal para convertir listas de palabras en una única cadena

# vamos a replicar esta url "https://www.google.com/search?q=curso+de+python+avanzado"

uri= "https://www.google.com/search?q="
tags = ["curso","de","python","avanzado"]
formatted_tags = '+'.join(tags)
query_uri = f'{uri}{formatted_tags}' 
print(query_uri)
