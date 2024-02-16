#Create (insertar) Read(Leer) Update (Actualizar) Delete (Eliminar)
#Crearemos un programa que permita manipular una lista, realizando las operaciones básicas

import os #Nos permite utilizar instrucciones de nuestro sistema operativo
import time

lista = []
while True:
    print('---MENU DEL SISTEMA---'
          '\n1.- Insertar dato'
          '\n2.- Eliminar un dato'
          '\n3.- Buscar un dato'
          '\n4.- Sobreescribir un dato'
          '\n5.- Mostrar el contenido de la lista'
          '\n6.- Salir del usuario')
    opcion = int(input('Elige una opcion: '))

    if (opcion == 1): #Create (Insertar)
        dato = input('Ingresar el dato a insertar: ')
        lista.append(dato)
        print('Dato insertado correctamente...')
        time.sleep(2)
        os.system('cls')
    elif (opcion == 2): #Delete (Eliminar)
        dato = input('Ingresar el dato a eliminar: ')

        if (dato in lista):
            lista.remove(dato)
            print('Dato eliminado correctamente...')
            time.sleep(2)
            os.system('cls')
        else:
            print('El dato a eliminar no se encontró en la estructura.')
            time.sleep(2)
            os.system('cls')
    elif (opcion == 3): #Read (Leer)
        dato = input('Ingresar el dato a buscar: ')

        if (dato in lista):
            print('El dato está en la lista, en la posicion:', lista.index(dato))
            time.sleep(2)
            os.system('cls')
        else:
            print('El dato no existe en la lista...')
            time.sleep(2)
            os.system('cls')
    elif (opcion == 4): #Update (Actualizar)
        datoAnterior = input('Ingresar el dato a sobreescribir: ')

        if (datoAnterior in lista):
            indice = lista.index(datoAnterior)
            datoNuevo = input('Ingresar el nuevo dato: ')
            lista[indice] = datoNuevo
            print('El dato se sobreescribió correctamente...')
            time.sleep(2)
            os.system('cls')
        else:
            print(f'El dato {datoAnterior} no existe en lista...')
            time.sleep(2)
            os.system('cls')
    elif (opcion == 5): #Read (Leer)
        print('El contenido de la lista es: ')
        print(lista)
        time.sleep(3)
        os.system('cls')
    elif (opcion == 6): #Salir del sistema
        respuesta = input('Esta segura? (s/n): ')

        if (respuesta.upper() == 'S'):
            print('Saliendo del sistema')
            time.sleep(2)
            os.system('cls')
            break
        time.sleep(2)
        os.system('cls')
    else:
        print('Opción no valida, intenta de nuevo...')
        time.sleep(2)
        os.system('cls')
