'''
Pediremos la estatura de una persona en cms y la evaluaremos:
. si mide menos de 160 cms dirá eres de estatura baja
. si mide entre 160 y 175 cms imprimirá eres de estatura media
. si mide mas de 175 cms imprimirá eres de estatura alta
'''

estatura = int(input('Escribe tu estatura en centimetros, por favor: '))

print(' ')

if (estatura < 160):
    print('Eres de estatura baja')

if (estatura >= 160 and estatura <= 175):
    print('Eres de estatura media')

#O tambien:
'''
if (estatura >= 160):
    if (estatura <= 175):
        print('Eres de estatura media')
'''

if (estatura > 175):
    print('Eres de estatura alta')