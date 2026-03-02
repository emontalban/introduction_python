#Acceder a una letra de una cadena

# E => 0
# l => 1
# ' ' => 2
# r => 3
sentence = 'El rapido zorro marron salto'

print(sentence[0]) 

#para acceder a un rango empieza por el ceroy acaba por la posicion 3 imprime 'El'

first_word = sentence[0:2]
new_sentence = first_word
print(new_sentence)

#vamos a remplazar salto por bailo

new_sentence = sentence.replace('salto', 'bailo')
print(new_sentence)

#vamos a cambiar una letra solo
change_sentence = 'El repido zorro marron salto'

change_sentence = change_sentence[0:4] + 'a' + change_sentence[5:]

print(change_sentence)

sentence = "Some pie please!"
sub_sentence = sentence[5:8]
print(sub_sentence)
