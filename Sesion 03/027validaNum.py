#El programa valida que solo se introduzcan números

while True:
    try:
        datos = input('Por favor ingresa tu edad: ')
        edad = int(datos)

        if (edad < 0):
            print('Edad no valida')
        else:
            break
    except ValueError:
        print('Error al capturar, por favor ingresa un dato númerico')
print('Edad valida:', edad)