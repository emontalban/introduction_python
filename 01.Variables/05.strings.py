#pangrama que contiene todas la letras del abecedario, una en español y otra en ingles

sentence_esp = "El veloz murciélago hindú comía feliz cardillo y kiwi; la cigüeña tocaba el saxofón detrás del palenque de paja."
sentence = "the quick brown fox jumped over the lazy dog" 

sentence_two = 'That is my dog\'s bowl'

sentence_three = "That is my dog's bowl"

sentence_four = "Tiffany said, \"That is my dog's bowl\""


print(sentence_esp)
print(sentence)
print(sentence_two)
print(sentence_three)
print(sentence_four)


# Poner todas las letras en mayusculas
sentence = "the quick brown fox jumped over the lazy dog" .upper()
sentence_two = "el murcielago comia feliz"
sentence_two.upper() # esto no funciona para solucionarlo hay que asignarlo a una variable o llamarlo en el print(sentence_two.upper())
print(sentence)
print(sentence_two)
print(sentence_two.upper())


# Poner todas la primera en mayusculas
sentence = "el murcielago comia feliz".capitalize()

print(sentence)

# Poner todas la mayusculas de la primera letra de cada palabra
sentence_two = "el murcielago comia feliz".title()

print(sentence_two)

# Poner todas las palabras en minusculas
sentence = "EL MURCIELAGO COMIA FELIZ".lower()

print(sentence)




