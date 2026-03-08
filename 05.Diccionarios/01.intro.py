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
        "extension": ".py"
    },

    "JavaScript": {
        "year": 1995,
        "creator": "Brendan Eich",
        "type": "interpretado",
        "paradigm": "multiparadigma",
        "popular_use": "desarrollo web",
        "extension": ".js"
    },

    "C": {
        "year": 1972,
        "creator": "Dennis Ritchie",
        "type": "compilado",
        "paradigm": "procedural",
        "popular_use": "sistemas operativos",
        "extension": ".c"
    },

    "Rust": {
        "year": 2010,
        "creator": "Graydon Hoare",
        "type": "compilado",
        "paradigm": "multiparadigma",
        "popular_use": "sistemas y seguridad",
        "extension": ".rs"
    },

    "Java": {
        "year": 1995,
        "creator": "James Gosling",
        "type": "compilado",
        "paradigm": "orientado a objetos",
        "popular_use": "aplicaciones empresariales y Android",
        "extension": ".java"
    },

    "C++": {
        "year": 1985,
        "creator": "Bjarne Stroustrup",
        "type": "compilado",
        "paradigm": "orientado a objetos / multiparadigma",
        "popular_use": "videojuegos y software de alto rendimiento",
        "extension": ".cpp"
    },

    "Go": {
        "year": 2009,
        "creator": "Google",
        "type": "compilado",
        "paradigm": "concurrente",
        "popular_use": "servidores y cloud",
        "extension": ".go"
    },

    "Swift": {
        "year": 2014,
        "creator": "Apple",
        "type": "compilado",
        "paradigm": "multiparadigma",
        "popular_use": "apps para iOS y macOS",
        "extension": ".swift"
    }
}
print(programming_languages)
print(programming_languages['Python'])
print(programming_languages['Python']['creator'])