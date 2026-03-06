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

# Acceder a los elemento rangos

print(programming_languages[1:3])   # accede a la posicion dos ya que el segundo numero no lo incluye
print(programming_languages[1:])    # Rango desde la posicion una hasta el final
print(programming_languages[:2])    # Rango desde la posicion cero haya la 1 ya que la dos no la incluye
print(programming_languages[:])     # Rango total de toda la lista
print(programming_languages[:-1])   # Rango de toda la lista menos el ultimo que no lo incluye
print(programming_languages[1:-1])  # Rango desde la posicion una hasta la posicion antes de la ultima 
print(programming_languages[:-1:2]) # Rango desde cero hasta la penultima y de dos en dos
print(programming_languages[::-1])  # Devuelve la misma lista pero a la inversa


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


