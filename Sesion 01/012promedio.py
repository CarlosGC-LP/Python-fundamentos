#El programa muestra y calcula el promedio de las calificaciones de un alumno

print('El programa calculara el promedio de tus 3 calificaciones\n')

nombre = input('Escribe tu nombre de alumno: ')
mat = float(input('Escribe tu calificacion de matematicas: '))
fis = float(input('Escribe tu calificacion de fisica: '))
quim = float(input('Escribe tu calificacion de quimica: '))

'''
prioridad de operadores aritmeticos
() y ** primer lugar
* y / segundo lugar
+ - tercer lugar
'''

prom = (mat + fis + quim) / 3

print(f'\n{nombre} tu promedio es: {round(prom, 2)}')