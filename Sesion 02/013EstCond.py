#Realiza un programa que avise al usuario si puede votar evaluando su edad

nombre = input('Escribe tu nombre: ')
edad = int(input('Escribe tu edad: '))

if (edad >= 18):
    print(nombre, 'ya puede votar, tiene:', edad, 'años')
else:
    print(nombre, 'no puede votar, tiene:', edad, 'años')