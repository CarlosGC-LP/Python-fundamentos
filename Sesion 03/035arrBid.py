#El programa manípula un arreglo bidimensional, tambien llamado matriz o lista de listas

#Creamos la matriz
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
#Como accedemos a un terminado elemento de una matriz?
elemento = matriz[1][2]
print('El elemento que esta en la fila 1 y columna 2 es:', elemento)

print('\nAhora recorremos toda la estructura: ')
for fila in matriz:
    for elemento in fila:
        print(elemento, end = ' ')
    print()