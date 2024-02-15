#Este programa pide un número y muestra su tabla de multiplicar

numero = int(input('Escribe un número y te mostraré su tabla de multiplicar'))

print('Tabla de multiplicar del número:', numero)

for i in range(1, 11):
    resultado = numero * i
    print(numero, 'x', i, '=', resultado)

#Plus
input('Presiona enter para continuar...')

print('\nAhora imprimiremos en orden invertido la tabla')
for i in range(10, 0, -1):
    resultado = numero * i
    print(numero, 'x', i, '=', resultado)