#Este programa pedirá datos, mientras los ingresados no estén entre el 1 y el 10

numero = 0

while True:
    numero = int(input('Escribe un número entre 1 y 10: '))

    if (numero >= 1) and (numero <= 10):
        break
    print('Número fuera de rango, intenta de nuevo')
print('Número válido ingresado:', numero)