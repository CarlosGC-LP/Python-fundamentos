#El programa manipula una lista con números y los ordena usando el método de ordenamiento llamado burbuja

datos = [50, 300, 27, 12, 9, 15]

print('La lista original es:', datos)

n = len(datos)

print('La longitud de la estructura es:', n)

for i in range(n - 1):
    for j in range(n - 1):
        print(f'i vale: {i} y j vale {j}')

        if (datos[j] > datos[j + 1]):
            datos[j], datos[j + 1] = datos[j + 1], datos[j]
            print('Actualmente, la lista es:', datos)
print('La lista ordenada es:', datos)