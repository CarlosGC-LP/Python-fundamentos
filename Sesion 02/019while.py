#Pediremos numeros y los iremos sumando en una variable, tecnicamente llamada acumulador, el programa terminará cuando el usuario digite un 0

suma = 0
numero = 1

while numero != 0:
    numero = int(input('Ingresa un numero para sumarlo, (ingresa 0 para salir): '))
    suma += numero
print('La suma total es:', suma)