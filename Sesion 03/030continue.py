#El programa solamente imprimirá el valor de la variable de control cuando esta sea impar

for i in range(1, 11):
    if i % 2 == 0:
        print('Impresión omitida por número par...')
        continue
    print(f'La variable i, vale: {i}')