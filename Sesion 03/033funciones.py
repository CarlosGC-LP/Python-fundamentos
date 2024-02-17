#El programa calculará el área de un circulo usando una función

import math

#Este es el código de nuestra función
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area
#Este es el código del programa y se ejecutará antes que la función
radio = float(input('Escribe el radio del circulo y calculará su área: '))

areaCir = calcular_area_circulo(radio)
print('El area del circulo es:', round(areaCir, 2))