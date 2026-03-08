# Los objetos de vista (o view objects) son estructuras de datos
# que proporcionan una vista dinámica de los elementos internos 
# de un diccionario (dict). Se generan al utilizar los métodos .keys(), 
# .values() o .items() en un diccionario.
# Proporciona una vista dinamica, lo que significa que cuando el diccionario cambia
# la vista refleja los cambios.

frameworks = {
    "Python": ["Django", "Flask", "FastAPI"],
    "JavaScript": ["React", "Angular", "Vue"],
    "Java": ["Spring", "Hibernate", "Struts"],
    "Rust": ["Rocket", "Actix"],
    "C++": ["Qt", "Boost"],
    "Go": ["Gin", "Beego"],
    "Swift": ["Vapor", "Kitura"],
    "Ruby": ["Ruby on Rails", "Sinatra", "Hanami"],
    "TypeScript": ["Angular", "NestJS"]
}

creators = {
    "Python": "Guido van Rossum",
    "JavaScript": "Brendan Eich",
    "C": "Dennis Ritchie",
    "Rust": "Graydon Hoare",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup",
    "Go": "Robert Griesemer, Rob Pike, Ken Thompson",
    "Swift": "Chris Lattner",
    "Ruby": "Yukihiro Matsumoto",
    "TypeScript": "Microsoft (Anders Hejlsberg)"
}

print(creators.keys())
print(creators.values())
print(creators.items())  # nos devuelve una tupla de clave valor

# para poder tratarla como una lista tradicional tenemos que convertirla en lista, 
# porque ahora no podemos acceder a ella tal y como esta, para acceder a un elemento

print(list(creators.keys())[1]) #accedemos al indice 1


#print(frameworks)