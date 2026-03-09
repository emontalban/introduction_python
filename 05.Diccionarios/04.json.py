## lista de diccionarios anidados estructura de un json

languages = [   
    {
        'Python': {
            "year": 1991,
            "creator": "Guido van Rossum",
            "frameworks": ["Django", "Flask", "FastAPI"]
        }    
    },
    {
        "JavaScript":{
            "year": 1995,
            "creator": "Brendan Eich",
            "frameworks": ["React", "Angular", "Vue"]
        }
    },
    {
        "Rust": {
            "year": 2010,
            "creator": "Graydon Hoare",
            "frameworks": ["Rocket", "Actix"]
        }
    }
]

print(languages[0])
print('----------------------------')
rust = languages[2].get('Rust', 'Language no found')
print(rust)
print(rust.values())    #ver los valores
print(list(rust.values())[1]) # para poder acceder a los indices hay que convertirlo en una lista

print('----------------------------')
print(languages)