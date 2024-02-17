#Crearemos una lista de listas que llenaremos desde el teclado

filas = 3
columnas = 3
matriz = [[1] * columnas for _ in range(filas)]

for i in range(filas):
    for j in range(columnas):
        dato = input('Ingresa el dato para la posicion ({}, {}): '.format(i, j))
        matriz[i][j] = dato
print('\nLos datos en la matriz son: ')
for fila in matriz:
    print(fila)
#Imprimir la diagonal principal
print('\nImprimiremos la diagonal principal')
for i in range(3):
    for j in range(3):
        if i == j:
            print(matriz[i][j])

#Imprimir la diagonal principal en orden inverso
print('\nImprimiremos la diagonal principal invertida')
for i in range(2, -1, -1):
    for j in range(2, -1, -1):
        if i == j:
            print(matriz[i][j])