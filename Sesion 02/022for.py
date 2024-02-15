import time

print('Imprimiremos la cadena de texto Hola mundo!' '\n utilizando el ciclo for')

for letra in 'Hola Mundo!':
    time.sleep(1)
    print(letra)
#Extra
nombre = input('Escribe tu nombre: ')
saludos = 'Hola '
saludoCompleto = saludos + nombre

print(' ')
for letra in saludoCompleto:
    time.sleep(1.5)
    print(letra)