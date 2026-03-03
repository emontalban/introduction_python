# Usamos el metodo find para encontrar la palabra 'quick' y nos devuelve 4
# que es la posiciocion en la que se encuentra

sentence = 'The quick brown fox jumped over the lazy dog'

query = sentence.find('quick') 

print(query)
# Resultado: 4


#--------------------------------------------------------------------------

# Index funciona igual que find a diferencia que si no encuentra da un error
# find si no lo encuentra da un -1

sentence = 'The quick brown fox jumped over the lazy dog'

query = sentence.index('quick') 

print(query)
# Resultado: 4

#--------------------------------------------------------------------------
# in nos devolvera true si existe y false si no
sentence = 'The quick brown fox jumped over the lazy dog'

query = 'fox' in sentence

print(query)
# Resultado: True