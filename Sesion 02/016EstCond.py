#El programa pedirá una cantidad en kilometros y la convertirá en metros o en centímetros

kms = float(input('Escribe la cantidad en kilometros: '))
opcion = input('Elige la opcion a convertir: '
               '\n a.- metros \n b.- centímetros')

if (opcion == 'a'):
    distancia = kms * 1000
elif (opcion == 'b'):
    distancia = kms * 100000
else:
    print('la opcion que elegiste, no es valida')
print('La distancia convertida es: ', distancia)