#El programa contiene un numero secreto que el usuario debe adivinar
#Se le avisará cuando lo logre o los intentos que quedan (3)

numero_secreto = 9
adivinado = False
intentos = 0
quedan = 3

while not(adivinado) and (intentos < 3):
    num = int(input('Adivina el numero (Es menor que 10): '))

    if (num == numero_secreto):
        print('Felicitaciones, has adivinado')
        adivinado = True
    else:
        intentos += 1

        if (intentos == 3):
            print('El juego ha terminado...')
        else:
            print('Por favor intenta de nuevo')
            quedan -= 1
            print('Te quedan', quedan, 'intentos')