# Python
## Variables 
Variables cuales son, como se utilizan y como son sus funciones
- Booleans
- Numbers
- Strings
- Bytes and byte arrays
- None
- Lists
- Tuples
- Sets
- Dictionaries

## Metodos de Strings
- Find
- Strip, LStrip, RStrip
- Partition
- Split
- isalpha, isnumeric

## Operadores en Python
### 1. Aritméticos (Matemáticos)
- + Suma: a + b
- - Resta: a - b
- * Multiplicación: a * b
- / División: a / b (siempre devuelve decimal)
- // División Entera: a // b (quita los decimales)
- % Módulo: a % b (el resto de la división)
- ** Exponente: a ** b (potencia)

### 2. Comparación (Relacionales)
- == Igual a: a == b
- != Distinto de: a != b
- > Mayor que: a > b
- < Menor que: a < b
- >= Mayor o igual: a >= b
- <= Menor o igual: a <= b

### 3. Lógicos
- and Y: Devuelve True si ambos son ciertos.
- or O: Devuelve True si al menos uno es cierto.
- not No: Invierte el valor booleano.

### 4. Asignación
- = Asignación simple: x = 5
- += Suma y asigna: x += 3 (equivale a x = x + 3)
- -= Resta y asigna: x -= 1
- *= Multiplica y asigna: x *= 2
- /= Divide y asigna x /= 2
- //= Divide y asigna y devuelve el numero entero y desecha decimales x //= 2
- **= Eleva a la potencia y asigna x **= 2
- %= Calcula modulo y asigna x %=2

### 5. Especiales
is Identidad: Comprueba si son el mismo objeto.
in Pertenencia: Comprueba si un valor está en una lista/cadena.

#### Tabla de operadores donde (X =200, y=6)

| Operador | Nombre                | Ejemplo      | Resultado          |
|----------|-----------------------|--------------|--------------------|
| +        | Suma                  | 200 + 6      | 206                |
| -        | Resta                 | 200 - 6      | 194                |
| *        | Multiplicación        | 200 * 6      | 1200               |
| /        | División              | 200 / 6      | 33.333333333333336 |
| //       | División entera       | 200 // 6     | 33                 |
| %        | Módulo (residuo)      | 200 % 6      | 2                  |
| **       | Potencia              | 200 ** 6     | 64000000000000     |

### Metodos con numeros
- math.sqrt
- math.floor
- math.ceil
- math.pow
- abs
- round

## Listas
- insert()
- append()
- remove()
- pop()
- del
- sort(), sort(reverse=True), sort(key=len), sort(key=str.lower)
- join()
- slice()
- extends()
- sorted()

## Dictionaries
 - keys()
 - values()
 - items()
 - del
 - pop()

### Dictionaries nested
```
lista
   │
   ├── diccionario
   │        └── diccionario
   │                └── lista
   │
   ├── diccionario
   │        └── diccionario
   │                └── lista
   │
   └── diccionario
            └── diccionario
                    └── lista
```

## Tuplas
Diccionario con tupla como clave

El uso de tuplas como claves en diccionarios de Python es una técnica que se emplea cuando necesitamos que la clave esté formada por más de un valor. Esto se llama clave compuesta. En lugar de usar una sola variable como identificador, usamos varios datos juntos agrupados en una tupla para identificar un elemento dentro del diccionario.

Porque usar tuplas:

- porque las claves deben de ser inmutables y las tuplas lo son.
- porque se necesita una clave compuesta que es una clave de mas de un atributo
- Cuando se usa una tupla para la clave se toma la tupla, se calcula un hash de la tupla,y se usa  es hash para encontrar el valor en 
la tabla de hash del diccionario

Ventajas:

Se podria oraganizar de otra manera como diccionarios anidados pero usar las tuplas  simplifica la estructura. Esto hace que sea mas directo
el codigo sea mas simple y las busquedas mas rapidas.

Cuando se usa la tupla como clave, el acceso  al valor se hace utilizando la misma tupla, Esto significa que el orden de los elementos en la tupla es importante

## Funcion zip()

La funcion zip() se utiliza para combinar valores iterables elemento a elemento. El resultado es un iterador de tupals donde cada tupla contiene los elemntos que estaban en la misma posicion en cada iterables. En otras palabras zip() empareja datos que estan en la misma posicion de distintas colecciones. 

Tomas dos o mas iterables y los agrupa en un indice, Çada  elemento del resultado es una tupla.

```
lista1:  A   B   C
lista2:  1   2   3
           │
           ▼
resultado:
(A,1) (B,2) (C,3)

```



## Conjuntos

Los conjuntos (Sets) son colecciones de datos que almacena elementos unicos, no existe duplicados, si se intenta añadir un elemento duplicado simplemente lo ignora, no tiene orden y es mutable, permite realizar operaciones matematicas  de conjuntos.

Los elementos dentro del set deben de ser inmutables por eso solo son validos (string, numeros y tuplas).

Los conjuntos no tienen indice, lo cual no se puede acceder a los elementos por el indice ya que no tiene posicion definida.

La forma correta de acceder al los elementos es iterando.

Una de las operaciones mas rapidad con conjuntos es verificar si un elemento esta dentro.

Para añadir elementos su puede usar add() y para eliminarlo remove()

Un set en Python es una colección no ordenada de elementos únicos, diseñada para eliminar duplicados y realizar operaciones matemáticas de conjuntos de forma rápida y eficiente.

Se utiliza mucho cuando necesitas:

- trabajar con elementos únicos
- hacer comparaciones entre colecciones
- realizar búsquedas rápidas.

Los Conjuntos permiten comparar colecciones de datos de forma muy eficiente, permitiendo saber rápidamente:

todos los elementos combinados (unión) |.
Une dos conjuntos y los unifica en uno eliminando los duplicados

los elementos comunes (intersección) &
la interseccion(&) devuelve los elementos que son comunes en ambos conjuntos

los elementos exclusivos de cada conjunto (diferencia) -
La diferencia (-) devuelve los elemntos que estan en el primer conjunto pero que no estan en el segundo, solo los exclusivos del primer elemento