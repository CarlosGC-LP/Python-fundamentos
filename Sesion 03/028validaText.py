#El programa valida entradas de tipo textow

while True:
    try:
        dato = input('Ingresa tu nombre de usuario: ')
        nombre = int(dato)
        print('Error, por favor ingresa solo texto, no números.')
    except ValueError:
        break
print('Nombre válido', dato)