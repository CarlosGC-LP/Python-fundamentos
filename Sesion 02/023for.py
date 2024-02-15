#El programa recorre un arreglo de números y se detiene
#La cantidad de segundos que indica el número

import time

for i in [.5, 3, 1, 4, .3, 2]:
    print(f'Retraso de {i} segundos')
    time.sleep(i)  