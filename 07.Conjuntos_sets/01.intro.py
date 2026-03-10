# Conjunto coleccion de datos que va entre llaves y no admite duplicacos
# no esta ordenado y es mutable

languages = {"Python", "JavaScript", "Rust", "Go", "Python"}

print(languages)
# imprimira Python solo una vez la segunda lo ignorara ya que es 
#conjunto

#comprobar si existe un elemento

print("Python" in languages)

#para acceder a los elementos se puede iterar para que te los muestre

for language in languages:
    print(language)

#para añadir un elemento con add()

languages.add("TypeScript")
print(languages)

# y para eliminarlo remove()

languages.remove("Go")
print(languages)

backend = {"Python", "Rust", "Go", "JavaScript","TypeScript"}
frontend ={"JavaScript", "TypeScript", "Python", "Css", "Html" }

#Union de conjuntos une los dos conjuntos eliminando duplicados
full_stack = backend | frontend
print(full_stack)

#Diferencia de conjuntos lo que devuelve es los elementos exclusivos del primer conjunto

full_stack = backend - frontend
print(full_stack)

# Interseccion (&)devuelve los elementos que estan en ambos conjuntos 

full_stack = backend & frontend
print(full_stack)