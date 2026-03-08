# Los diccionarios en Python son estructuras de datos que almacenan
# pares ordenados de clave-valor (key:value), permitiendo búsquedas
# rápidas y eficientes. Son mutables, dinámicos (pueden cambiar de tamaño) y utilizan llaves {}.
# Las claves deben ser únicas e inmutables (como cadenas o números).
# es sensible a mayusculas o minusculas y si no encuentra la clave da un error

programming_languages = {
    "Python": {
        "year": 1991,
        "creator": "Guido van Rossum",
        "type": "interpretado",
        "paradigm": "multiparadigma",
        "popular_use": "data science, IA, automatización",
        "extension": ".py",
        "frameworks": ["Django", "Flask", "FastAPI"]
    },

    "JavaScript": {
        "year": 1995,
        "creator": "Brendan Eich",
        "type": "interpretado",
        "paradigm": "multiparadigma",
        "popular_use": "desarrollo web",
        "extension": ".js",
        "frameworks": ["React", "Angular", "Vue"]
    },

    "C": {
        "year": 1972,
        "creator": "Dennis Ritchie",
        "type": "compilado",
        "paradigm": "procedural",
        "popular_use": "sistemas operativos",
        "extension": ".c",
        "frameworks": ["GTK", "glib"]
    },

    "Rust": {
        "year": 2010,
        "creator": "Graydon Hoare",
        "type": "compilado",
        "paradigm": "multiparadigma",
        "popular_use": "sistemas y seguridad",
        "extension": ".rs",
        "frameworks": ["Rocket", "Actix"]
    },

    "Java": {
        "year": 1995,
        "creator": "James Gosling",
        "type": "compilado",
        "paradigm": "orientado a objetos",
        "popular_use": "aplicaciones empresariales y Android",
        "extension": ".java",
        "frameworks": ["Spring", "Hibernate", "Struts"]
    },

    "C++": {
        "year": 1985,
        "creator": "Bjarne Stroustrup",
        "type": "compilado",
        "paradigm": "multiparadigma",
        "popular_use": "videojuegos y software de alto rendimiento",
        "extension": ".cpp",
        "frameworks": ["Qt", "Boost"]
    },

    "Go": {
        "year": 2009,
        "creator": "Google",
        "type": "compilado",
        "paradigm": "concurrente",
        "popular_use": "servidores y cloud",
        "extension": ".go",
        "frameworks": ["Gin", "Beego"]
    },

    "Swift": {
        "year": 2014,
        "creator": "Apple",
        "type": "compilado",
        "paradigm": "multiparadigma",
        "popular_use": "apps para iOS y macOS",
        "extension": ".swift",
        "frameworks": ["Vapor", "Kitura"]
    }
}


print(programming_languages)
print(programming_languages['Python'])
print(programming_languages['Python']['creator']) # Guido van Rossum
print(programming_languages['Python']['frameworks'][1]) # Flask
print(programming_languages['Python']['frameworks'][::-1]) # ['FastAPI', 'Flask', 'Django']

#añadimos un nuevo lenguaje
programming_languages["Kotlin"] = {
    "year": 2011,
    "creator": "JetBrains",
    "type": "compilado",
    "paradigm": "multiparadigma",
    "popular_use": "apps Android",
    "extension": ".kt",
    "frameworks": ["Ktor", "Spring"]
}

print(programming_languages)

# añadimos un nuevo  framework a python

programming_languages["Python"]["libraries"] = ["NumPy", "Pandas", "Matplotlib"]

print(programming_languages['Python'])

# Para evitar que de error si no existe podemos poner uno por defecto 

perfect_languages= programming_languages.get('TypeScript', 'No prefect_languages')
print(perfect_languages)



programming_languages["JavaScript"]["libraries"] = ["Lodash", "Axios", "Moment.js"]
programming_languages["Java"]["libraries"] = ["Guava", "Apache Commons", "JUnit"]
programming_languages["Rust"]["libraries"] = ["Serde", "Tokio", "Reqwest"]