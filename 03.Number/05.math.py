import math
# La librería math eofrece funciones matemáticas avanzadas Algunas de las funciones ofrecidas son:

loss = -20.25 
product_cost = 89.99

# abs()
# Devuelve el valor absoluto de un numero (sin signo negativo)
# Convierte números negativos en positivos.
print(abs(loss)) # 20.25

# math.floor()
# Redondea hacia abajo al entero mas cercano.
print(math.floor(product_cost)) # 89

# math.ceil()
# Redondea hacia arriba al entero mas cercano
print(math.ceil(product_cost)) # 90

# Redondea el numero  y lo convierte en positivo
print(abs(math.floor(loss))) # 21

# Redondea al entero mas cercano
print(round(product_cost)) # 90

# Calcula la raíz cuadrada.
print(math.sqrt(product_cost))  # 9.486305919587455

# Eleva un número a una potencia.
print(math.pow(5, 2))  # devuelve un float 25.0
print(5 ** 2)          # devuelve un int 25

print(abs(-45))



