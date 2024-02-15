#Este programa pide al usuario numeros para sumarlos, y promediarlos para salir debe ingresarse -1

contador = 0
suma = 0
numero = 0

while True:
    numero = int(input('Ingresa un número para sumarlo (-1 para salir): '))

    if (numero == -1):
        break
    suma += numero
    contador += 1
print(' ')
if (contador > 0):
    promedio = suma / contador
    print('La suma de los números introducidos es:', suma)
    print('La cantidad de números introducidos es:', contador)
    print('El promedio de número ingresado es:', promedio)
else:
    print('No se ingresaron números válidos...')