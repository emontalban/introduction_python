#STRIP sirve para eliminar 

#en este caso nos elimina los espacios de delante y de detras

url = '                 https://www.google.com                   '


print(url.strip())

#En este caso elimina  https://
url = 'https://www.google.com'


print(url.strip('https://'))

#Tambien podemos usea lstrip (left strip) y  rstrip (right strip)
#En este ejemplo queremos que nos devuelva Google

url = 'https://www.google.com'

url = url.lstrip('https://www.')
url = url.rstrip('.com')
url = url.capitalize()

print(url)

