# Como cambiar valores a a las variables
#example

meal_completed = True
sub_total = 100
tip = sub_total * 1/5
total = sub_total + tip
receipt = "Your total is " + str(total)
print(receipt)


#Cambiamos el subtotal por total y ahora empezamos todo desdes al variable total
meal_completed = True
total = 100
tip = total * 0.20
total = total + tip
receipt = "Your total is " + str(total)
print(receipt)

#Nuevo ejemplo cambiamos el valor de la variable second
first = 'Anna'
second = 'Keira'
third = 'Deidra'

print(second)

second = 'Niamh'

print(second)