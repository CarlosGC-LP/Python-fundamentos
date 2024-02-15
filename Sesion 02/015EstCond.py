'''
Pediremos una cantidad en dólares, mostraremos un menú para
realizar conversiones:

1.- Convertir en Pesos Mexicanos
2.- Convertir en Soles Peruanos

y mostraremos el resultado de la conversión
'''

dolares = float(input('Escribe la cantidad en dolares a convertir: '))
opcion = int(input('A cual moneda los quieres convertir: '
                   '\n 1.- Pesos \n 2.- Soles'))

if (opcion == 1):
    total = dolares * 16.5
    print('La cantidad convertida en pesos mexicanos es: ', total)
elif (opcion == 2):
    total = dolares * 3.80
    print('La cantidad convertida en soles peruanos es: ', total)
else:
    print('La opción que elegiste no es válida, intenta de nuevo')