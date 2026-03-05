# Es una colección de valores a la que se le pueden añadir, 
# eliminar, consultar y modificar elementos dentro de ella.
# Los elementos van separados por comas y estan dentro de un corchete []
# se puede acceder mediante indices numericos empezando por cero [0]

programming_languages = ["Python","Java","Ruby","Go","Swift"]

print(programming_languages)

# El método insert(índice, elemento)  un nuevo elemento en una posición específica (índice) 
# de una lista, desplazando los elementos existentes hacia la derecha.

programming_languages.insert(0,"kotlin")

print(programming_languages)

# El método append() en Python se utiliza para añadir un solo elemento al final de una lista existente

programming_languages.append("JavaScript")

print(programming_languages)


# Acceder a los elementos 

print(programming_languages[0]) # devuelve el objeto de la primera posicion
print([programming_languages[0]]) # devuelve una lista con elemento de la primera posicion


programming_languages[4] = "Rust"  # otra manera de reasignar los elementos

print(programming_languages)


# Eliminar elementos

# El método .remove() elimina la primera aparición de un valor específico
# de una lista. Modifica la lista original directamente y, si el elemento no se encuentra, 
# lanza un error de tipo ValueError. Solo elimina el primer elemento que coincide con el valor,
# no todos los duplicados

programming_languages.remove('kotlin')

print(programming_languages)

# El método .pop() elimina y devuelve un elemento de una lista,
#  modificando la lista original. Por defecto, elimina el último elemento 
# si no se especifica un índice, o el elemento en la posición pop(indice) indicada.
#  Es fundamental para trabajar con el valor eliminado o implementar pilas

# "del" es otra forma de borrar elementos pasando la posicion
# a diferencia de remove() del no devuelve el elemento eliminado simplemento lo borra de la memoria

del programming_languages[3]

print(programming_languages)
