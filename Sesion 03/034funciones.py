#Crearemos una función que reciba un numero y determine si es o no par
def es_par(num):
    if (num % 2 == 0):
        return True
    else:
        return False
numero = int(input('Escribe un número y determiné si es par o impar: '))

if es_par(numero):
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')