# Eliminar elementos del diccionario con DEL


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

# Esto funciona cuando sabes que existe esa clave y la escribe teniendo en cuenta
# las mayusculas y minusculas sino te dara error
del frameworks ['Go']

print(frameworks)

# El método pop() en un diccionario de Python elimina una clave específica (key)
# y devuelve su valor asociado. Si la clave no existe, lanza un error KeyError, 
# a menos que se proporcione un valor predeterminado como segundo argumento (pop(key, default))

frameworks.pop('PHP','Lenguaje no encontrado')
frameworks.pop('TypeScript','Lenguaje no encontrado')
print(frameworks)

## lista de diccionarios anidados

languages = [
    {
        "name": "Python",
        "year": 1991,
        "creator": "Guido van Rossum",
        "frameworks": ["Django", "Flask", "FastAPI"]
    },
    {
        "name": "JavaScript",
        "year": 1995,
        "creator": "Brendan Eich",
        "frameworks": ["React", "Angular", "Vue"]
    },
    {
        "name": "Rust",
        "year": 2010,
        "creator": "Graydon Hoare",
        "frameworks": ["Rocket", "Actix"]
    }
]

print(languages)