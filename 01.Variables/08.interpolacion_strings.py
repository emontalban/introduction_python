#Example one

name = 'keira'
greeting = f'Hi {name}'
print (greeting)

#Example two

name= 'Keira'
product = 'Python learning course'

email_content = f"""
Hi {name}

Thank you for purchasing {product}

Regards,

Sales Team
"""

print(email_content)

#example Three

name = 'Keira'
age = 12
product = 'Python eLearning course'
farewell = 'Bye'

greeting_one = "Product Purchase: {2} - Hi {0}, you are listed as {1} years old. - {3}".format(name, age, product, 'Bye')

greeting_two = f"Product Purchase: {product} - Hi {name}, you are listed as {age} years old. - {farewell}"

print(greeting_one, greeting_two)
